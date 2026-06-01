'use strict';
require('dotenv').config();
const express   = require('express');
const cors      = require('cors');
const helmet    = require('helmet');
const morgan    = require('morgan');
const path      = require('path');
const twilio    = require('twilio');
const VoiceResponse = twilio.twiml.VoiceResponse;

const { loadConfig }    = require('./business-config');
const genderDetector    = require('./gender-detector');
const appointments      = require('./appointments');
const receptionist      = require('./receptionist');
const voiceService      = require('./voice-service');

const app    = express();
const config = loadConfig();
const PORT   = process.env.PORT || 3000;
const BASE_URL = process.env.BASE_URL || `http://localhost:${PORT}`;

// ── Middleware ────────────────────────────────────────────────────────────────

app.use(helmet({ contentSecurityPolicy: false }));
app.use(cors());
app.use(morgan('dev'));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use('/audio', express.static(path.join(__dirname, 'public', 'audio')));
app.use(express.static(path.join(__dirname, '..', 'public')));

// ── Twilio Signatur-Validierung (Produktion) ─────────────────────────────────

function validateTwilio(req, res, next) {
  if (process.env.NODE_ENV !== 'production') return next();
  const valid = twilio.validateRequest(
    process.env.TWILIO_AUTH_TOKEN,
    req.headers['x-twilio-signature'] || '',
    `${BASE_URL}${req.originalUrl}`,
    req.body
  );
  if (!valid) return res.status(403).send('Ungültige Twilio-Signatur');
  next();
}

// ═══════════════════════════════════════════════════════════════════════════════
//  TWILIO VOICE WEBHOOKS
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * POST /voice/incoming
 * Eingehender Anruf – Begrüßung und ersten Gather starten.
 */
app.post('/voice/incoming', validateTwilio, async (req, res) => {
  const callSid     = req.body.CallSid;
  const callerPhone = req.body.From || '';
  const twiml       = new VoiceResponse();

  console.log(`[Call] Eingehend: ${callerPhone} | SID: ${callSid}`);

  try {
    const greetingText = await receptionist.generateGreeting(callSid, config, callerPhone);
    const tts = await voiceService.synthesize(greetingText);

    if (tts) {
      twiml.play(tts.url);
    } else {
      twiml.say({ voice: 'Polly.Vicki', language: 'de-DE' }, greetingText);
    }

    const gather = twiml.gather({
      input:        'speech',
      action:       `${BASE_URL}/voice/process`,
      method:       'POST',
      language:     'de-DE',
      speechTimeout: 'auto',
      timeout:      5,
      enhanced:     'true',
    });
    gather.pause({ length: 1 });

    // Falls keine Eingabe kommt → erneut fragen
    twiml.redirect(`${BASE_URL}/voice/no-input`);

  } catch (err) {
    console.error('[Voice] Fehler bei Begrüßung:', err);
    twiml.say({ voice: 'Polly.Vicki', language: 'de-DE' },
      `${config.greeting} Bitte sprechen Sie nach dem Signal.`);
    twiml.gather({ input: 'speech', action: `${BASE_URL}/voice/process`, method: 'POST',
                   language: 'de-DE', speechTimeout: 'auto' });
  }

  res.type('text/xml').send(twiml.toString());
});

/**
 * POST /voice/process
 * Spracheingabe verarbeiten und KI-Antwort zurückgeben.
 */
app.post('/voice/process', validateTwilio, async (req, res) => {
  const callSid       = req.body.CallSid;
  const callerPhone   = req.body.From || '';
  const speechResult  = req.body.SpeechResult || '';
  const confidence    = parseFloat(req.body.Confidence || '0');
  const twiml         = new VoiceResponse();

  console.log(`[Voice] Input (${Math.round(confidence * 100)}%): "${speechResult}"`);

  if (!speechResult.trim()) {
    return res.redirect(307, `${BASE_URL}/voice/no-input`);
  }

  try {
    const result = await receptionist.processInput(callSid, speechResult, callerPhone, config);

    // Anruf-Log aktualisieren
    appointments.logCall({
      callSid,
      callerPhone,
      gender:        result.gender,
      intent:        result.intent,
      appointmentId: result.appointmentId,
      transcript:    speechResult,
    });

    const tts = await voiceService.synthesize(result.text);
    if (tts) {
      twiml.play(tts.url);
    } else {
      twiml.say({ voice: 'Polly.Vicki', language: 'de-DE' }, result.text);
    }

    if (result.shouldHangup) {
      twiml.hangup();
    } else {
      const gather = twiml.gather({
        input:         'speech',
        action:        `${BASE_URL}/voice/process`,
        method:        'POST',
        language:      'de-DE',
        speechTimeout: 'auto',
        timeout:       6,
        enhanced:      'true',
      });
      gather.pause({ length: 1 });
      twiml.redirect(`${BASE_URL}/voice/no-input`);
    }

  } catch (err) {
    console.error('[Voice] Fehler bei Verarbeitung:', err);
    twiml.say({ voice: 'Polly.Vicki', language: 'de-DE' },
      'Entschuldigung, es gab einen technischen Fehler. Ich verbinde Sie weiter.');
    twiml.hangup();
  }

  res.type('text/xml').send(twiml.toString());
});

/**
 * POST /voice/no-input
 * Keine Spracheingabe erkannt – erneut nachfragen.
 */
app.post('/voice/no-input', validateTwilio, async (req, res) => {
  const twiml = new VoiceResponse();
  const msg   = 'Entschuldigung, ich habe Sie nicht verstanden. Wie kann ich Ihnen helfen?';
  const tts   = await voiceService.synthesize(msg).catch(() => null);

  if (tts) twiml.play(tts.url);
  else twiml.say({ voice: 'Polly.Vicki', language: 'de-DE' }, msg);

  twiml.gather({
    input:         'speech',
    action:        `${BASE_URL}/voice/process`,
    method:        'POST',
    language:      'de-DE',
    speechTimeout: 'auto',
    timeout:       6,
  });
  twiml.hangup();

  res.type('text/xml').send(twiml.toString());
});

/**
 * POST /voice/status
 * Anruf-Status-Callback von Twilio.
 */
app.post('/voice/status', (req, res) => {
  const { CallSid, CallStatus, CallDuration, From } = req.body;
  console.log(`[Status] ${CallSid}: ${CallStatus} (${CallDuration}s)`);

  if (CallStatus === 'completed' || CallStatus === 'no-answer') {
    appointments.logCall({
      callSid:     CallSid,
      callerPhone: From || '',
      durationSec: parseInt(CallDuration || '0'),
    });
    receptionist.clearSession(CallSid);
    genderDetector.clearCall(CallSid);
  }
  res.sendStatus(200);
});

// ═══════════════════════════════════════════════════════════════════════════════
//  REST API – TERMINE
// ═══════════════════════════════════════════════════════════════════════════════

function requireAdmin(req, res, next) {
  const secret = process.env.ADMIN_SECRET;
  if (!secret) return next(); // kein Schutz in Entwicklung
  const provided = req.headers['x-admin-secret'] || req.query.secret;
  if (provided !== secret) return res.status(401).json({ error: 'Nicht autorisiert' });
  next();
}

// Alle Termine abrufen
app.get('/api/appointments', requireAdmin, (req, res) => {
  const list = appointments.listAppointments({
    date:     req.query.date,
    status:   req.query.status,
    upcoming: req.query.upcoming === 'true',
  });
  res.json(list);
});

// Termin erstellen (manuell via Dashboard)
app.post('/api/appointments', requireAdmin, (req, res) => {
  try {
    const appt = appointments.createAppointment(req.body);
    res.status(201).json(appt);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Termin abrufen
app.get('/api/appointments/:id', requireAdmin, (req, res) => {
  const appt = appointments.getAppointment(req.params.id);
  if (!appt) return res.status(404).json({ error: 'Nicht gefunden' });
  res.json(appt);
});

// Termin stornieren
app.delete('/api/appointments/:id', requireAdmin, (req, res) => {
  const appt = appointments.cancelAppointment(req.params.id, req.body?.reason || '');
  if (!appt) return res.status(404).json({ error: 'Nicht gefunden' });
  res.json(appt);
});

// Termin verschieben
app.patch('/api/appointments/:id', requireAdmin, (req, res) => {
  const { date, time } = req.body;
  const appt = appointments.rescheduleAppointment(req.params.id, date, time);
  if (!appt) return res.status(404).json({ error: 'Nicht gefunden' });
  res.json(appt);
});

// Freie Zeitslots
app.get('/api/availability', requireAdmin, (req, res) => {
  const { service, days } = req.query;
  const slots = appointments.getAvailableDays(service, config.services, config.hours, parseInt(days || '14'));
  res.json(slots);
});

// ═══════════════════════════════════════════════════════════════════════════════
//  REST API – DASHBOARD
// ═══════════════════════════════════════════════════════════════════════════════

// Statistiken
app.get('/api/stats', requireAdmin, (req, res) => {
  res.json(appointments.getStats());
});

// Anruf-Logs
app.get('/api/calls', requireAdmin, (req, res) => {
  res.json(appointments.getCallLogs(parseInt(req.query.limit || '50')));
});

// Unternehmens-Konfiguration
app.get('/api/config', requireAdmin, (req, res) => {
  res.json({
    name:     config.name,
    type:     config.type,
    label:    config.label,
    emoji:    config.emoji,
    phone:    config.phone,
    email:    config.email,
    address:  config.address,
    services: config.services,
    hours:    config.hours,
    language: config.language,
  });
});

// ElevenLabs Stimmen
app.get('/api/voices', requireAdmin, async (req, res) => {
  const voices = await voiceService.getRecommendedVoices();
  res.json(voices);
});

// Gesundheitsprüfung
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    business: config.name,
    type: config.type,
    timestamp: new Date().toISOString(),
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
//  SERVER START
// ═══════════════════════════════════════════════════════════════════════════════

app.listen(PORT, () => {
  console.log(`
╔══════════════════════════════════════════════════════╗
║       KI-Telefonempfang – Server gestartet           ║
╠══════════════════════════════════════════════════════╣
║  Unternehmen : ${config.name.padEnd(37)}║
║  Branche     : ${config.label.padEnd(37)}║
║  Port        : ${String(PORT).padEnd(37)}║
║  Basis-URL   : ${BASE_URL.padEnd(37)}║
║                                                      ║
║  Twilio Webhook → ${(BASE_URL + '/voice/incoming').padEnd(33)}║
╚══════════════════════════════════════════════════════╝
  `);
});

module.exports = app;
