'use strict';
require('dotenv').config();
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

const ELEVENLABS_API = 'https://api.elevenlabs.io/v1';
const AUDIO_DIR = path.join(__dirname, 'public', 'audio');

// Sicherstellen, dass Audio-Verzeichnis existiert
if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });

// ── Cache für häufige Phrasen ────────────────────────────────────────────────

const phraseCache = new Map();

// ── ElevenLabs TTS ───────────────────────────────────────────────────────────

/**
 * Text mit ElevenLabs in Sprache umwandeln.
 * Gibt den Dateipfad und die öffentliche URL zurück.
 */
async function synthesize(text, options = {}) {
  const apiKey   = process.env.ELEVENLABS_API_KEY;
  const voiceId  = options.voiceId  || process.env.ELEVENLABS_VOICE_ID  || 'EXAVITQu4vr4xnSDxMaL';
  const modelId  = options.modelId  || process.env.ELEVENLABS_MODEL_ID  || 'eleven_multilingual_v2';
  const baseUrl  = process.env.BASE_URL || 'http://localhost:3000';

  if (!apiKey) {
    console.warn('[TTS] Kein ElevenLabs API-Schlüssel – verwende Twilio Say');
    return null;
  }

  // Cache prüfen
  const cacheKey = `${voiceId}::${text.trim()}`;
  if (phraseCache.has(cacheKey)) {
    const cached = phraseCache.get(cacheKey);
    if (fs.existsSync(cached.filePath)) {
      return cached;
    }
  }

  try {
    const response = await axios.post(
      `${ELEVENLABS_API}/text-to-speech/${voiceId}`,
      {
        text,
        model_id: modelId,
        voice_settings: {
          stability:        options.stability        ?? 0.55,
          similarity_boost: options.similarityBoost  ?? 0.80,
          style:            options.style            ?? 0.25,
          use_speaker_boost: true,
        },
      },
      {
        headers: {
          'xi-api-key':     apiKey,
          'Content-Type':   'application/json',
          'Accept':         'audio/mpeg',
        },
        responseType: 'arraybuffer',
        timeout: 15000,
      }
    );

    const filename = `tts_${uuidv4()}.mp3`;
    const filePath = path.join(AUDIO_DIR, filename);
    fs.writeFileSync(filePath, Buffer.from(response.data));

    // Alte Dateien aufräumen (> 5 Min)
    _cleanupOldAudio();

    const result = { filePath, url: `${baseUrl}/audio/${filename}`, filename };
    phraseCache.set(cacheKey, result);
    return result;

  } catch (err) {
    console.error('[TTS] ElevenLabs Fehler:', err.response?.status, err.message);
    return null;
  }
}

/**
 * Verfügbare ElevenLabs-Stimmen abrufen.
 */
async function listVoices() {
  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) return [];
  try {
    const resp = await axios.get(`${ELEVENLABS_API}/voices`, {
      headers: { 'xi-api-key': apiKey },
    });
    return resp.data.voices || [];
  } catch {
    return [];
  }
}

/**
 * Deutsche weibliche Empfehlungen aus vorhandenen Stimmen.
 */
async function getRecommendedVoices() {
  const voices = await listVoices();
  return voices.filter(v =>
    v.labels?.language === 'de' ||
    v.labels?.gender === 'female' ||
    ['Sarah', 'Charlotte', 'Lena', 'Paula', 'Nicole'].includes(v.name)
  );
}

// ── TwiML-Hilfsfunktionen ────────────────────────────────────────────────────

/**
 * TwiML <Say> Tag mit deutschen Einstellungen (Fallback ohne ElevenLabs).
 */
function twimlSay(text, options = {}) {
  const voice    = options.voice    || 'Polly.Vicki';
  const language = options.language || 'de-DE';
  return `<Say voice="${voice}" language="${language}">${_escapeXml(text)}</Say>`;
}

/**
 * TwiML <Play> für ElevenLabs-Audio oder <Say> als Fallback.
 */
async function twimlSpeak(text, gatherAction = null) {
  const tts = await synthesize(text);
  const speakTag = tts
    ? `<Play>${_escapeXml(tts.url)}</Play>`
    : twimlSay(text);

  if (!gatherAction) return speakTag;

  return `
    ${speakTag}
    <Gather input="speech" action="${gatherAction}" method="POST"
            language="de-DE" speechTimeout="auto" timeout="5"
            enhanced="true" speechModel="phone_call">
    </Gather>`;
}

// ── Interne Hilfsfunktionen ──────────────────────────────────────────────────

function _escapeXml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function _cleanupOldAudio() {
  try {
    const files = fs.readdirSync(AUDIO_DIR);
    const maxAge = 5 * 60 * 1000; // 5 Minuten
    for (const f of files) {
      if (!f.startsWith('tts_')) continue;
      const fp = path.join(AUDIO_DIR, f);
      const stat = fs.statSync(fp);
      if (Date.now() - stat.mtimeMs > maxAge) fs.unlinkSync(fp);
    }
  } catch { /* ignorieren */ }
}

module.exports = { synthesize, listVoices, getRecommendedVoices, twimlSay, twimlSpeak };
