'use strict';
require('dotenv').config();

// ── Branchenspezifische Vorlagen ────────────────────────────────────────────

const INDUSTRY_TEMPLATES = {
  friseur: {
    label: 'Friseursalon',
    emoji: '✂️',
    aiPersonality: 'freundlich, modebewusst und kompetent',
    greeting: 'Herzlich willkommen beim {name}! Sie haben uns angerufen, wie kann ich Ihnen helfen?',
    services: [
      { id: 'schnitt_damen', name: 'Damenhaarschnitt', duration: 60, price: 45 },
      { id: 'schnitt_herren', name: 'Herrenhaarschnitt', duration: 30, price: 25 },
      { id: 'farbe', name: 'Coloration / Färben', duration: 120, price: 80 },
      { id: 'strähnchen', name: 'Strähnchen / Highlights', duration: 150, price: 95 },
      { id: 'dauerwelle', name: 'Dauerwelle', duration: 120, price: 75 },
      { id: 'pflege', name: 'Haarpflege-Behandlung', duration: 45, price: 35 },
      { id: 'styling', name: 'Föhnen & Styling', duration: 30, price: 20 },
      { id: 'kind', name: 'Kinderhaarschnitt', duration: 30, price: 18 },
    ],
    keywords: ['haare', 'schnitt', 'färben', 'frisur', 'shampoo', 'styling'],
  },

  arzt: {
    label: 'Arztpraxis',
    emoji: '🩺',
    aiPersonality: 'einfühlsam, professionell und diskret',
    greeting: 'Praxis {name}, guten Tag! Was kann ich für Sie tun?',
    services: [
      { id: 'erstgespraech', name: 'Erstgespräch / Neupatient', duration: 30, price: 0 },
      { id: 'vorsorge', name: 'Vorsorgeuntersuchung', duration: 45, price: 0 },
      { id: 'akut', name: 'Akutsprechstunde', duration: 20, price: 0 },
      { id: 'beratung', name: 'Beratungsgespräch', duration: 20, price: 0 },
      { id: 'impfung', name: 'Impftermin', duration: 15, price: 0 },
      { id: 'blutabnahme', name: 'Blutabnahme', duration: 15, price: 0 },
      { id: 'kontrolle', name: 'Kontrolluntersuchung', duration: 20, price: 0 },
    ],
    keywords: ['schmerzen', 'krank', 'rezept', 'überweisung', 'untersuchung', 'krankenkasse'],
    specialNote: 'Bei medizinischen Notfällen bitte sofort 112 anrufen.',
  },

  restaurant: {
    label: 'Restaurant / Café',
    emoji: '🍽️',
    aiPersonality: 'herzlich, gastfreundlich und enthusiastisch',
    greeting: 'Restaurant {name}, guten Tag! Wie kann ich Ihnen helfen?',
    services: [
      { id: 'tisch_2', name: 'Tischreservierung (2 Personen)', duration: 120, price: 0 },
      { id: 'tisch_4', name: 'Tischreservierung (4 Personen)', duration: 120, price: 0 },
      { id: 'tisch_gruppe', name: 'Gruppenreservierung (ab 6 Personen)', duration: 180, price: 0 },
      { id: 'event', name: 'Private Veranstaltung / Feier', duration: 240, price: 0 },
    ],
    keywords: ['tisch', 'reservierung', 'speisekarte', 'vegetarisch', 'vegan', 'allergie'],
  },

  anwalt: {
    label: 'Rechtsanwaltskanzlei',
    emoji: '⚖️',
    aiPersonality: 'seriös, präzise und vertrauenswürdig',
    greeting: 'Kanzlei {name}, guten Tag! Wie kann ich Ihnen behilflich sein?',
    services: [
      { id: 'erstberatung', name: 'Erstberatung (30 Min.)', duration: 30, price: 90 },
      { id: 'beratung_std', name: 'Rechtsberatung (60 Min.)', duration: 60, price: 180 },
      { id: 'mandatsgespräch', name: 'Mandatsgespräch', duration: 60, price: 180 },
      { id: 'telefonberatung', name: 'Telefonische Beratung', duration: 30, price: 90 },
    ],
    keywords: ['recht', 'klage', 'vertrag', 'scheidung', 'erbschaft', 'arbeitsrecht'],
    specialNote: 'Alle Gespräche sind selbstverständlich vertraulich.',
  },

  physiotherapie: {
    label: 'Physiotherapie / Massage',
    emoji: '💆',
    aiPersonality: 'ruhig, gesundheitsbewusst und fürsorglich',
    greeting: 'Praxis {name}, guten Tag! Wie kann ich Ihnen helfen?',
    services: [
      { id: 'physiotherapie', name: 'Physiotherapie (Einzelbehandlung)', duration: 45, price: 60 },
      { id: 'massage_30', name: 'Klassische Massage (30 Min.)', duration: 30, price: 40 },
      { id: 'massage_60', name: 'Klassische Massage (60 Min.)', duration: 60, price: 70 },
      { id: 'rueckenmassage', name: 'Rückenmassage', duration: 45, price: 55 },
      { id: 'krankengymnastik', name: 'Krankengymnastik', duration: 30, price: 45 },
      { id: 'manualtherapie', name: 'Manualtherapie', duration: 45, price: 65 },
    ],
    keywords: ['rücken', 'schmerzen', 'massage', 'entspannung', 'krankenkasse', 'rezept'],
  },

  kosmetik: {
    label: 'Kosmetikstudio / Beauty',
    emoji: '💄',
    aiPersonality: 'glamourös, selbstbewusst und kundenorientiert',
    greeting: 'Studio {name}, hallo! Wie kann ich Ihnen helfen?',
    services: [
      { id: 'gesichtsbehandlung', name: 'Gesichtsbehandlung', duration: 60, price: 65 },
      { id: 'peeling', name: 'Peeling & Reinigung', duration: 45, price: 50 },
      { id: 'wimpern', name: 'Wimpernverlängerung', duration: 120, price: 120 },
      { id: 'augenbrauen', name: 'Augenbrauen formen & färben', duration: 45, price: 35 },
      { id: 'make_up', name: 'Make-up (inkl. Hochzeit)', duration: 90, price: 80 },
      { id: 'microneedling', name: 'Microneedling', duration: 60, price: 95 },
    ],
    keywords: ['haut', 'pflege', 'make-up', 'wimpern', 'gesicht', 'anti-aging'],
  },

  nagelstudio: {
    label: 'Nagelstudio',
    emoji: '💅',
    aiPersonality: 'trendy, kreativ und freundlich',
    greeting: '{name}, hallo! Wie kann ich Ihnen weiterhelfen?',
    services: [
      { id: 'gelnägel', name: 'Gelnägel Neuaufbau', duration: 90, price: 60 },
      { id: 'gel_auffüllen', name: 'Gelnägel Auffüllen', duration: 60, price: 45 },
      { id: 'maniküre', name: 'Klassische Maniküre', duration: 45, price: 35 },
      { id: 'pediküre', name: 'Pediküre', duration: 60, price: 45 },
      { id: 'nageldesign', name: 'Nageldesign / Nail Art', duration: 30, price: 25 },
      { id: 'acryl', name: 'Acrylnägel', duration: 90, price: 65 },
    ],
    keywords: ['nägel', 'gel', 'acryl', 'design', 'french', 'shellac'],
  },

  zahnarzt: {
    label: 'Zahnarztpraxis',
    emoji: '🦷',
    aiPersonality: 'beruhigend, professionell und verständnisvoll',
    greeting: 'Zahnarztpraxis {name}, guten Tag! Wie kann ich Ihnen helfen?',
    services: [
      { id: 'kontrolle', name: 'Vorsorgeuntersuchung', duration: 30, price: 0 },
      { id: 'reinigung', name: 'Professionelle Zahnreinigung', duration: 60, price: 100 },
      { id: 'fuellen', name: 'Zahnfüllung', duration: 60, price: 0 },
      { id: 'akut', name: 'Akutbehandlung / Zahnschmerzen', duration: 30, price: 0 },
      { id: 'beratung', name: 'Beratungsgespräch', duration: 20, price: 0 },
      { id: 'roentgen', name: 'Röntgenaufnahme', duration: 20, price: 0 },
    ],
    keywords: ['zahn', 'zahnschmerzen', 'karies', 'wurzelbehandlung', 'krone', 'implantat'],
    specialNote: 'Bei starken Zahnschmerzen bieten wir Notfalltermine an.',
  },

  fitness: {
    label: 'Fitness / Yoga / Sport',
    emoji: '🏋️',
    aiPersonality: 'motiviert, energetisch und unterstützend',
    greeting: '{name}, hallo! Wie kann ich Ihnen helfen?',
    services: [
      { id: 'probetermin', name: 'Probestunde (kostenlos)', duration: 60, price: 0 },
      { id: 'pt_session', name: 'Personal Training (60 Min.)', duration: 60, price: 75 },
      { id: 'yogakurs', name: 'Yoga-Kurs (60 Min.)', duration: 60, price: 18 },
      { id: 'pilates', name: 'Pilates-Kurs', duration: 55, price: 18 },
      { id: 'ernaehrungsberatung', name: 'Ernährungsberatung', duration: 60, price: 80 },
      { id: 'koerperanalyse', name: 'Körperanalyse', duration: 30, price: 30 },
    ],
    keywords: ['training', 'abnehmen', 'yoga', 'kurs', 'mitgliedschaft', 'muskel'],
  },

  werkstatt: {
    label: 'Autowerkstatt / KFZ',
    emoji: '🔧',
    aiPersonality: 'kompetent, zuverlässig und direkt',
    greeting: 'Werkstatt {name}, guten Tag! Was kann ich für Sie tun?',
    services: [
      { id: 'inspektion', name: 'Hauptinspektion', duration: 120, price: 180 },
      { id: 'oel', name: 'Ölwechsel', duration: 45, price: 80 },
      { id: 'tuev', name: 'TÜV / HU Vorbereitung', duration: 60, price: 90 },
      { id: 'reifen', name: 'Reifenwechsel (4 Reifen)', duration: 60, price: 60 },
      { id: 'bremsen', name: 'Bremsenservice', duration: 90, price: 150 },
      { id: 'diagnose', name: 'Fehlerdiagnose', duration: 45, price: 50 },
      { id: 'klima', name: 'Klimaanlage befüllen', duration: 60, price: 80 },
    ],
    keywords: ['auto', 'motor', 'bremsen', 'reifen', 'tüv', 'inspektion', 'öl'],
  },

  allgemein: {
    label: 'Allgemeiner Service',
    emoji: '🏢',
    aiPersonality: 'professionell, freundlich und hilfsbereit',
    greeting: 'Willkommen bei {name}! Wie kann ich Ihnen helfen?',
    services: [
      { id: 'beratung', name: 'Beratungsgespräch', duration: 30, price: 0 },
      { id: 'termin', name: 'Allgemeiner Termin', duration: 60, price: 0 },
    ],
    keywords: [],
  },
};

// ── Standard-Öffnungszeiten ──────────────────────────────────────────────────

const DEFAULT_HOURS = {
  monday:    { open: '09:00', close: '18:00', closed: false },
  tuesday:   { open: '09:00', close: '18:00', closed: false },
  wednesday: { open: '09:00', close: '18:00', closed: false },
  thursday:  { open: '09:00', close: '18:00', closed: false },
  friday:    { open: '09:00', close: '17:00', closed: false },
  saturday:  { open: '10:00', close: '14:00', closed: false },
  sunday:    { open: null,    close: null,    closed: true  },
};

// ── Konfiguration laden ──────────────────────────────────────────────────────

function loadConfig() {
  const type = (process.env.BUSINESS_TYPE || 'allgemein').toLowerCase();
  const template = INDUSTRY_TEMPLATES[type] || INDUSTRY_TEMPLATES.allgemein;
  const name = process.env.BUSINESS_NAME || 'Unser Unternehmen';

  return {
    name,
    type,
    label: template.label,
    emoji: template.emoji,
    phone: process.env.BUSINESS_PHONE || '',
    email: process.env.BUSINESS_EMAIL || '',
    address: process.env.BUSINESS_ADDRESS || '',
    aiPersonality: template.aiPersonality,
    greeting: template.greeting.replace('{name}', name),
    farewell: `Vielen Dank für Ihren Anruf bei ${name}. Einen schönen Tag noch! Auf Wiederhören.`,
    services: template.services,
    keywords: template.keywords,
    specialNote: template.specialNote || null,
    hours: DEFAULT_HOURS,
    language: process.env.LANGUAGE || 'de',
  };
}

module.exports = { loadConfig, INDUSTRY_TEMPLATES };
