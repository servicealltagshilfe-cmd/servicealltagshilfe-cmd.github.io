'use strict';
const Database = require('better-sqlite3');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

const DB_PATH = path.join(__dirname, 'data', 'appointments.db');

let db;

function getDb() {
  if (!db) {
    db = new Database(DB_PATH);
    db.pragma('journal_mode = WAL');
    db.pragma('foreign_keys = ON');
    _initSchema();
  }
  return db;
}

function _initSchema() {
  db.exec(`
    CREATE TABLE IF NOT EXISTS appointments (
      id          TEXT PRIMARY KEY,
      service_id  TEXT NOT NULL,
      service_name TEXT NOT NULL,
      duration    INTEGER NOT NULL,
      customer_name TEXT NOT NULL,
      customer_phone TEXT,
      customer_email TEXT,
      gender      TEXT DEFAULT 'unknown',
      date        TEXT NOT NULL,
      time        TEXT NOT NULL,
      datetime_iso TEXT NOT NULL,
      status      TEXT DEFAULT 'confirmed',
      notes       TEXT DEFAULT '',
      created_at  TEXT NOT NULL,
      call_sid    TEXT
    );

    CREATE TABLE IF NOT EXISTS blocked_slots (
      id         TEXT PRIMARY KEY,
      date       TEXT NOT NULL,
      time_start TEXT NOT NULL,
      time_end   TEXT NOT NULL,
      reason     TEXT DEFAULT 'Blockiert'
    );

    CREATE TABLE IF NOT EXISTS call_logs (
      id          TEXT PRIMARY KEY,
      call_sid    TEXT NOT NULL,
      caller_phone TEXT,
      gender      TEXT DEFAULT 'unknown',
      duration_sec INTEGER DEFAULT 0,
      intent      TEXT,
      appointment_id TEXT,
      transcript  TEXT,
      started_at  TEXT NOT NULL,
      ended_at    TEXT
    );
  `);
}

// ── Zeitslots berechnen ──────────────────────────────────────────────────────

function getAvailableSlots(date, serviceDuration, businessHours) {
  const db = getDb();
  const dayNames = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'];
  const d = new Date(date + 'T00:00:00');
  const dayName = dayNames[d.getDay()];
  const hours = businessHours[dayName];

  if (!hours || hours.closed) return [];

  const [openH, openM]   = hours.open.split(':').map(Number);
  const [closeH, closeM] = hours.close.split(':').map(Number);
  const openMinutes  = openH * 60 + openM;
  const closeMinutes = closeH * 60 + closeM;

  const existing = db.prepare(
    'SELECT time, duration FROM appointments WHERE date = ? AND status != ?'
  ).all(date, 'cancelled');

  const blocked = db.prepare(
    'SELECT time_start, time_end FROM blocked_slots WHERE date = ?'
  ).all(date);

  const occupiedRanges = [
    ...existing.map(a => {
      const [h, m] = a.time.split(':').map(Number);
      const start = h * 60 + m;
      return { start, end: start + a.duration };
    }),
    ...blocked.map(b => {
      const [sh, sm] = b.time_start.split(':').map(Number);
      const [eh, em] = b.time_end.split(':').map(Number);
      return { start: sh * 60 + sm, end: eh * 60 + em };
    }),
  ];

  const slots = [];
  for (let t = openMinutes; t + serviceDuration <= closeMinutes; t += 15) {
    const overlaps = occupiedRanges.some(r => t < r.end && t + serviceDuration > r.start);
    if (!overlaps) {
      const h = Math.floor(t / 60).toString().padStart(2, '0');
      const m = (t % 60).toString().padStart(2, '0');
      slots.push(`${h}:${m}`);
    }
  }
  return slots;
}

function getAvailableDays(serviceId, services, businessHours, daysAhead = 14) {
  const duration = services.find(s => s.id === serviceId)?.duration || 30;
  const result = [];
  for (let i = 1; i <= daysAhead; i++) {
    const d = new Date();
    d.setDate(d.getDate() + i);
    const dateStr = d.toISOString().split('T')[0];
    const slots = getAvailableSlots(dateStr, duration, businessHours);
    if (slots.length > 0) {
      result.push({ date: dateStr, slots: slots.slice(0, 6) }); // max 6 Vorschläge
    }
  }
  return result;
}

// ── CRUD ─────────────────────────────────────────────────────────────────────

function createAppointment({ serviceId, serviceName, duration, customerName,
  customerPhone, customerEmail, gender, date, time, notes, callSid }) {
  const db = getDb();
  const id = uuidv4();
  const datetimeIso = new Date(`${date}T${time}:00`).toISOString();

  db.prepare(`
    INSERT INTO appointments
    (id, service_id, service_name, duration, customer_name, customer_phone,
     customer_email, gender, date, time, datetime_iso, status, notes, created_at, call_sid)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
  `).run(id, serviceId, serviceName, duration, customerName, customerPhone || '',
    customerEmail || '', gender || 'unknown', date, time, datetimeIso,
    'confirmed', notes || '', new Date().toISOString(), callSid || null);

  return getAppointment(id);
}

function getAppointment(id) {
  return getDb().prepare('SELECT * FROM appointments WHERE id = ?').get(id);
}

function listAppointments({ date, status, upcoming } = {}) {
  const db = getDb();
  let query = 'SELECT * FROM appointments WHERE 1=1';
  const params = [];

  if (date)     { query += ' AND date = ?';     params.push(date); }
  if (status)   { query += ' AND status = ?';   params.push(status); }
  if (upcoming) { query += ' AND datetime_iso >= ?'; params.push(new Date().toISOString()); }

  query += ' ORDER BY datetime_iso ASC';
  return db.prepare(query).all(...params);
}

function cancelAppointment(id, reason = '') {
  const db = getDb();
  const a = getAppointment(id);
  if (!a) return null;
  db.prepare('UPDATE appointments SET status = ?, notes = ? WHERE id = ?')
    .run('cancelled', (a.notes ? a.notes + ' | ' : '') + `Storniert: ${reason}`, id);
  return getAppointment(id);
}

function rescheduleAppointment(id, newDate, newTime) {
  const db = getDb();
  const a = getAppointment(id);
  if (!a) return null;
  const datetimeIso = new Date(`${newDate}T${newTime}:00`).toISOString();
  db.prepare('UPDATE appointments SET date = ?, time = ?, datetime_iso = ?, status = ? WHERE id = ?')
    .run(newDate, newTime, datetimeIso, 'rescheduled', id);
  return getAppointment(id);
}

function findAppointmentByPhone(phone, upcoming = true) {
  const db = getDb();
  const baseQuery = upcoming
    ? 'SELECT * FROM appointments WHERE customer_phone = ? AND datetime_iso >= ? AND status != ? ORDER BY datetime_iso ASC LIMIT 5'
    : 'SELECT * FROM appointments WHERE customer_phone = ? ORDER BY datetime_iso DESC LIMIT 5';

  return upcoming
    ? db.prepare(baseQuery).all(phone, new Date().toISOString(), 'cancelled')
    : db.prepare(baseQuery).all(phone);
}

// ── Anruf-Logs ───────────────────────────────────────────────────────────────

function logCall({ callSid, callerPhone, gender, intent, appointmentId, transcript, durationSec }) {
  const db = getDb();
  const existing = db.prepare('SELECT id FROM call_logs WHERE call_sid = ?').get(callSid);
  if (existing) {
    db.prepare(`UPDATE call_logs SET gender=?, intent=?, appointment_id=?, transcript=?,
      duration_sec=?, ended_at=? WHERE call_sid=?`)
      .run(gender || 'unknown', intent || '', appointmentId || null,
        transcript || '', durationSec || 0, new Date().toISOString(), callSid);
  } else {
    db.prepare(`INSERT INTO call_logs
      (id, call_sid, caller_phone, gender, intent, appointment_id, transcript, duration_sec, started_at)
      VALUES (?,?,?,?,?,?,?,?,?)`)
      .run(uuidv4(), callSid, callerPhone || '', gender || 'unknown',
        intent || '', appointmentId || null, transcript || '',
        durationSec || 0, new Date().toISOString());
  }
}

function getCallLogs(limit = 20) {
  return getDb().prepare('SELECT * FROM call_logs ORDER BY started_at DESC LIMIT ?').all(limit);
}

// ── Statistiken ──────────────────────────────────────────────────────────────

function getStats() {
  const db = getDb();
  const today = new Date().toISOString().split('T')[0];
  const weekStart = new Date();
  weekStart.setDate(weekStart.getDate() - weekStart.getDay());
  const weekStr = weekStart.toISOString().split('T')[0];

  return {
    totalAppointments:     db.prepare('SELECT COUNT(*) AS c FROM appointments').get().c,
    todayAppointments:     db.prepare('SELECT COUNT(*) AS c FROM appointments WHERE date = ?').get(today).c,
    weekAppointments:      db.prepare('SELECT COUNT(*) AS c FROM appointments WHERE date >= ?').get(weekStr).c,
    cancelledToday:        db.prepare("SELECT COUNT(*) AS c FROM appointments WHERE date = ? AND status = 'cancelled'").get(today).c,
    totalCalls:            db.prepare('SELECT COUNT(*) AS c FROM call_logs').get().c,
    femaleCalls:           db.prepare("SELECT COUNT(*) AS c FROM call_logs WHERE gender = 'female'").get().c,
    maleCalls:             db.prepare("SELECT COUNT(*) AS c FROM call_logs WHERE gender = 'male'").get().c,
    upcomingAppointments:  db.prepare('SELECT COUNT(*) AS c FROM appointments WHERE datetime_iso >= ? AND status = ?').get(new Date().toISOString(), 'confirmed').c,
  };
}

module.exports = {
  getAvailableSlots,
  getAvailableDays,
  createAppointment,
  getAppointment,
  listAppointments,
  cancelAppointment,
  rescheduleAppointment,
  findAppointmentByPhone,
  logCall,
  getCallLogs,
  getStats,
};
