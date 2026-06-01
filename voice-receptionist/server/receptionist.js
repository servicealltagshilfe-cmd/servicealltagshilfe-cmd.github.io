'use strict';
require('dotenv').config();
const Anthropic = require('@anthropic-ai/sdk');
const genderDetector = require('./gender-detector');
const appointments = require('./appointments');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

// ── Gesprächs-Sessions ───────────────────────────────────────────────────────

const sessions = new Map();

function getSession(callSid) {
  if (!sessions.has(callSid)) {
    sessions.set(callSid, {
      callSid,
      gender: 'unknown',
      messages: [],
      bookingState: null, // { step, serviceId, serviceName, duration, date, time, name }
      resolvedAppointmentId: null,
      callerPhone: null,
      createdAt: Date.now(),
    });
  }
  return sessions.get(callSid);
}

function clearSession(callSid) {
  sessions.delete(callSid);
}

// ── Systempromt ──────────────────────────────────────────────────────────────

function buildSystemPrompt(config, gender) {
  const salutation = genderDetector.getGermanSalutation(gender);
  const salutationNote = salutation
    ? `Du sprichst mit einer ${gender === 'female' ? 'Frau' : 'einem Mann'}. Verwende die Anrede "${salutation}" wenn du den Nachnamen kennst.`
    : 'Das Geschlecht der anrufenden Person ist noch unbekannt. Bleibe neutral (z.B. "Guten Tag!" statt "Guten Tag, Herr/Frau X").';

  const serviceList = config.services
    .map(s => `  • ${s.name} (${s.duration} Min.${s.price ? `, ab ${s.price}€` : ''}) [ID: ${s.id}]`)
    .join('\n');

  const now = new Date();
  const dateStr = now.toLocaleDateString('de-DE', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
  const timeStr = now.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });

  return `Du bist "Lisa", die KI-Empfangsdame für "${config.name}" (${config.label}).
Deine Persönlichkeit: ${config.aiPersonality}, warm und professionell.
Aktuelles Datum: ${dateStr}, ${timeStr} Uhr.

${salutationNote}

DEINE AUFGABEN:
1. Anrufer begrüßen und ihren Wunsch verstehen
2. Termine vereinbaren, verschieben oder stornieren
3. Auskunft über Leistungen, Preise und Öffnungszeiten geben
4. Bei komplexen Fragen: Rückruf durch Mensch ankündigen

VERFÜGBARE LEISTUNGEN:
${serviceList}
${config.specialNote ? `\nWICHTIG: ${config.specialNote}` : ''}

TERMINBUCHUNGS-WORKFLOW:
Wenn jemand einen Termin möchte:
1. Welche Leistung gewünscht? → Aus der Liste oben wählen
2. Bevorzugtes Datum/Uhrzeit? → Prüfe Verfügbarkeit
3. Name des Kunden erfragen
4. Termin bestätigen: "Ich buche für Sie: [Leistung] am [Datum] um [Uhrzeit] Uhr."

STORNIERUNG:
- "Termin stornieren" → Telefonnummer oder Datum/Uhrzeit erfragen → bestätigen

SPRACHREGELN (KRITISCH für Telefon):
- Antworten KURZ halten (max. 2-3 Sätze pro Turn)
- Immer EINE klare Frage stellen, nie mehrere
- Vermeide Listen und Aufzählungen – sprich natürlich
- Wenn Termin gebucht: Gib Datum und Uhrzeit klar auf Deutsch aus (z.B. "Montag, der 5. Juli um 14 Uhr")
- Spreche IMMER auf Deutsch

INTENTS die du erkennen und als JSON-Tag am Ende ausgeben musst:
Nach jeder Antwort füge einen unsichtbaren Marker an:
[INTENT:greet|book|cancel|reschedule|info|done|transfer]
[BOOKING_STATE:none|collecting_service|collecting_datetime|collecting_name|confirming|complete]
[SERVICE_ID:service_id_oder_none]`;
}

// ── Absichts-Parsing ─────────────────────────────────────────────────────────

function parseMetadata(text) {
  const intentMatch    = text.match(/\[INTENT:([^\]]+)\]/);
  const stateMatch     = text.match(/\[BOOKING_STATE:([^\]]+)\]/);
  const serviceMatch   = text.match(/\[SERVICE_ID:([^\]]+)\]/);

  return {
    intent:       intentMatch?.[1]  || 'info',
    bookingState: stateMatch?.[1]   || 'none',
    serviceId:    serviceMatch?.[1] !== 'none' ? serviceMatch?.[1] : null,
    cleanText:    text
      .replace(/\[INTENT:[^\]]+\]/g, '')
      .replace(/\[BOOKING_STATE:[^\]]+\]/g, '')
      .replace(/\[SERVICE_ID:[^\]]+\]/g, '')
      .trim(),
  };
}

// ── Datum/Uhrzeit aus Text extrahieren ───────────────────────────────────────

function extractDatetime(text) {
  const now = new Date();

  // "morgen", "übermorgen"
  if (/morgen früh|morgen/i.test(text)) {
    const d = new Date(now); d.setDate(d.getDate() + 1);
    return { date: d.toISOString().split('T')[0], time: null };
  }
  if (/übermorgen/i.test(text)) {
    const d = new Date(now); d.setDate(d.getDate() + 2);
    return { date: d.toISOString().split('T')[0], time: null };
  }

  // Wochentage
  const weekdays = { montag:1, dienstag:2, mittwoch:3, donnerstag:4, freitag:5, samstag:6, sonntag:0 };
  for (const [name, idx] of Object.entries(weekdays)) {
    if (new RegExp(`\\b${name}\\b`, 'i').test(text)) {
      const d = new Date(now);
      const diff = (idx - d.getDay() + 7) % 7 || 7;
      d.setDate(d.getDate() + diff);
      return { date: d.toISOString().split('T')[0], time: null };
    }
  }

  // Datum: "am 15. Juli" oder "15.07." oder "15. 07."
  const datePattern = /(\d{1,2})[.\s]+(\d{1,2}|\w+)[.\s]*(?:(\d{4}))?/;
  const dateMatch = text.match(datePattern);
  if (dateMatch) {
    const day   = parseInt(dateMatch[1]);
    const month = parseInt(dateMatch[2]) || _monthFromName(dateMatch[2]);
    const year  = parseInt(dateMatch[3]) || now.getFullYear();
    if (day && month) {
      const d = new Date(year, month - 1, day);
      return { date: d.toISOString().split('T')[0], time: null };
    }
  }

  return { date: null, time: null };
}

function extractTime(text) {
  // "um 14 Uhr", "um 14:30", "halb 3", "viertel nach 10"
  const match = text.match(/(\d{1,2})(?::(\d{2}))?\s*Uhr/i);
  if (match) {
    const h = match[1].padStart(2, '0');
    const m = (match[2] || '00').padStart(2, '0');
    return `${h}:${m}`;
  }
  const halfMatch = text.match(/halb\s+(\d{1,2})/i);
  if (halfMatch) {
    const h = (parseInt(halfMatch[1]) - 1).toString().padStart(2, '0');
    return `${h}:30`;
  }
  return null;
}

function _monthFromName(name) {
  const months = { jan:1, feb:2, mär:3, mar:3, apr:4, mai:5, jun:6,
                   jul:7, aug:8, sep:9, okt:10, nov:11, dez:12 };
  const lower = (name || '').toLowerCase().slice(0, 3);
  return months[lower] || null;
}

// ── Verfügbarkeits-Zusammenfassung für KI ────────────────────────────────────

function formatAvailabilityForAI(slots) {
  if (!slots.length) return 'Leider sind in den nächsten zwei Wochen keine freien Termine verfügbar.';
  const lines = slots.slice(0, 4).map(({ date, slots: times }) => {
    const d = new Date(date + 'T00:00:00');
    const label = d.toLocaleDateString('de-DE', { weekday: 'long', day: 'numeric', month: 'long' });
    return `${label}: ${times.slice(0, 3).join(' Uhr, ')} Uhr`;
  });
  return 'Freie Termine:\n' + lines.join('\n');
}

// ── Hauptverarbeitungsfunktion ────────────────────────────────────────────────

/**
 * Eine Spracheingabe verarbeiten und KI-Antwort zurückgeben.
 *
 * @param {string} callSid - Twilio Call SID
 * @param {string} userInput - Transkribierter Text des Anrufers
 * @param {string} callerPhone - Telefonnummer des Anrufers
 * @param {object} config - Unternehmens-Konfiguration
 * @returns {{ text, intent, shouldHangup, appointmentId }}
 */
async function processInput(callSid, userInput, callerPhone, config) {
  const session = getSession(callSid);
  session.callerPhone = callerPhone;

  // Geschlechts-Erkennung aus Text
  const textGender = genderDetector.detectFromText(userInput);
  const gender = genderDetector.updateAndGetGender(callSid, textGender);
  session.gender = gender;

  // Nachricht zum Verlauf hinzufügen
  session.messages.push({ role: 'user', content: userInput });

  // Verfügbare Termine laden wenn im Buchungsprozess
  let availabilityContext = '';
  if (session.bookingState?.step === 'collecting_datetime' && session.bookingState.serviceId) {
    const service = config.services.find(s => s.id === session.bookingState.serviceId);
    if (service) {
      const slots = appointments.getAvailableDays(
        service.id, config.services, config.hours
      );
      availabilityContext = `\n\nAKTUELLE VERFÜGBARKEIT für "${service.name}":\n${formatAvailabilityForAI(slots)}`;
    }
  }

  // Buchungs-Kontext als User-Hinweis
  let bookingContext = '';
  if (session.bookingState) {
    const bs = session.bookingState;
    bookingContext = `\n[Aktueller Buchungsstatus: Schritt="${bs.step}", Service="${bs.serviceName || ''}", Datum="${bs.date || ''}", Uhrzeit="${bs.time || ''}", Name="${bs.name || ''}"]`;
  }

  // Anrufer-Info für Stornierung
  const existingAppointments = callerPhone
    ? appointments.findAppointmentByPhone(callerPhone, true)
    : [];
  const existingApptContext = existingAppointments.length > 0
    ? `\n[Bestehende Termine des Anrufers: ${existingAppointments.map(a =>
        `${a.service_name} am ${a.date} um ${a.time} Uhr (ID: ${a.id})`
      ).join('; ')}]`
    : '';

  const systemPrompt = buildSystemPrompt(config, gender) + availabilityContext + bookingContext + existingApptContext;

  // Claude aufrufen
  const response = await client.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 400,
    system: systemPrompt,
    messages: session.messages,
  });

  const rawText = response.content[0].text;
  const { intent, bookingState, serviceId, cleanText } = parseMetadata(rawText);

  // Antwort zum Verlauf hinzufügen
  session.messages.push({ role: 'assistant', content: rawText });

  // Buchungsstatus aktualisieren
  _updateBookingState(session, intent, bookingState, serviceId, userInput, config);

  // Termin erstellen wenn vollständig
  let appointmentId = null;
  if (bookingState === 'complete' && session.bookingState) {
    const bs = session.bookingState;
    if (bs.serviceId && bs.date && bs.time && bs.name) {
      try {
        const service = config.services.find(s => s.id === bs.serviceId);
        const appt = appointments.createAppointment({
          serviceId:    bs.serviceId,
          serviceName:  bs.serviceName || service?.name || 'Termin',
          duration:     service?.duration || 30,
          customerName: bs.name,
          customerPhone: callerPhone || '',
          gender,
          date: bs.date,
          time: bs.time,
          callSid,
        });
        appointmentId = appt.id;
        session.resolvedAppointmentId = appt.id;
        session.bookingState = null;
      } catch (err) {
        console.error('[Booking] Fehler beim Erstellen:', err.message);
      }
    }
  }

  // Stornierung verarbeiten
  if (intent === 'cancel' && existingAppointments.length > 0) {
    const apptIdInText = userInput.match(/[0-9a-f-]{36}/)?.[0];
    if (apptIdInText) {
      appointments.cancelAppointment(apptIdInText);
    } else if (existingAppointments.length === 1) {
      appointments.cancelAppointment(existingAppointments[0].id);
    }
  }

  const shouldHangup = intent === 'done' || cleanText.toLowerCase().includes('auf wiederhören');

  return {
    text:          cleanText,
    intent,
    gender,
    shouldHangup,
    appointmentId,
    sessionMessages: session.messages.length,
  };
}

function _updateBookingState(session, intent, bookingStateStr, serviceId, userInput, config) {
  if (intent === 'book' && !session.bookingState) {
    session.bookingState = { step: 'collecting_service', serviceId: null, serviceName: null, date: null, time: null, name: null };
  }

  if (!session.bookingState) return;

  const bs = session.bookingState;

  // Service auswählen
  if (serviceId && serviceId !== 'none') {
    bs.serviceId = serviceId;
    const svc = config.services.find(s => s.id === serviceId);
    bs.serviceName = svc?.name || serviceId;
    bs.step = 'collecting_datetime';
  }

  // Datum/Zeit extrahieren
  if (bs.step === 'collecting_datetime' || bs.step === 'collecting_service') {
    const { date } = extractDatetime(userInput);
    const time = extractTime(userInput);
    if (date) bs.date = date;
    if (time) bs.time = time;
    if (bs.date && bs.time) bs.step = 'collecting_name';
  }

  // Name extrahieren
  const nameMatch = userInput.match(/(?:ich heiße|mein name ist|ich bin|für)\s+([A-ZÄÖÜ][a-zäöüß]+(?: [A-ZÄÖÜ][a-zäöüß]+)?)/i);
  if (nameMatch && !bs.name) {
    bs.name = nameMatch[1];
    bs.step = 'confirming';
  }

  // Bestätigung
  if (bs.step === 'confirming' && /\b(ja|gerne|stimmt|korrekt|richtig|gut|okay|ok|bitte)\b/i.test(userInput)) {
    bs.step = 'complete';
  }

  if (bookingStateStr === 'complete') {
    bs.step = 'complete';
  }
}

/**
 * Begrüßungstext beim ersten Anruf generieren.
 */
async function generateGreeting(callSid, config, callerPhone) {
  const existingAppt = callerPhone
    ? appointments.findAppointmentByPhone(callerPhone, true)
    : [];

  let greetingHint = '';
  if (existingAppt.length > 0) {
    const a = existingAppt[0];
    const d = new Date(a.date + 'T' + a.time);
    greetingHint = ` Ich sehe, Sie haben einen Termin für ${a.service_name} am ${d.toLocaleDateString('de-DE', { weekday: 'long', day: 'numeric', month: 'long' })} um ${a.time} Uhr.`;
  }

  const greeting = config.greeting + greetingHint;
  const session = getSession(callSid);
  session.messages.push({ role: 'assistant', content: greeting + ' [INTENT:greet][BOOKING_STATE:none][SERVICE_ID:none]' });
  return greeting;
}

module.exports = { processInput, generateGreeting, clearSession, getSession };
