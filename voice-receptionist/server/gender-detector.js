'use strict';

// ── Deutsche Vornamen-Datenbank ──────────────────────────────────────────────

const FEMALE_NAMES = new Set([
  'anna','maria','laura','julia','sarah','lisa','lena','emma','sophie','mia',
  'lea','hannah','sophia','nina','claudia','andrea','sabine','karin','susanne',
  'christine','barbara','petra','monika','ulrike','ingrid','helga','gertrud',
  'brigitte','ursula','elfriede','hildegard','edeltraud','waltraud','lieselotte',
  'charlotte','marie','luisa','emilia','johanna','leonie','amelie','clara',
  'amelie','friederike','josephine','katharina','magdalena','theresa','veronika',
  'natalie','jessica','stefanie','angela','martina','birgit','renate','elke',
  'gisela','irmgard','christel','marianne','ilse','hannelore','heidi','sigrid',
  'roswitha','dagmar','anke','bettina','silke','tanja','anja','nadine','melanie',
  'jennifer','michelle','vanessa','stephanie','nicole','diana','katja','mandy',
  'celine','zoe','lara','amelie','luise','nora','jule','greta','lilli','maja',
  'frieda','paula','rosa','ida','hanna','selina','jasmin','lisa-marie',
  'annalena','annabell','annika','antonia','arabella','ariane','astrid',
  'beatrix','bernadette','bettina','brunhild','cecilia','cornelia','edith',
  'erika','eva','franziska','gerda','gudrun','gundula','hedwig','heike',
  'ines','iris','isolde','jessica','juliane','jutta','karoline','kirsten',
  'klara','konstanze','kornelia','kristina','lieselotte','lotte','luise',
  'magda','margarete','margot','marlene','martina','mathilde','miriam',
  'nadja','nathalie','ortrud','patricia','petra','rosi','rut','sabrina',
  'samira','senta','sigrid','sonia','sonja','sylvia','tamara','tina',
  'trude','ute','walburga','wilhelmine','yasmin','yvonne','zweitname',
]);

const MALE_NAMES = new Set([
  'thomas','michael','andreas','stefan','christian','daniel','markus','martin',
  'johannes','wolfgang','hans','karl','friedrich','walter','herbert','heinz',
  'werner','günter','horst','gerhard','helmut','dieter','jürgen','hans-jürgen',
  'hans-peter','frank','peter','bernd','ulrich','rainer','hans-dieter',
  'alexander','felix','maximilian','jonas','lukas','jakob','leon','noah',
  'tim','jan','nico','ben','david','paul','simon','julian','tobias',
  'sebastian','philipp','fabian','florian','patrick','marc','marco',
  'oliver','dominik','kevin','dennis','mario','mario','nils','sven',
  'bastian','benedikt','bernhard','boris','christoph','claus','dietrich',
  'edgar','egbert','egon','elmar','emmerich','erhard','ernst','eugen',
  'finn','florian','franz','fritz','georg','gerd','gottfried','gregor',
  'hannes','harold','hartmut','henning','henry','holger','hubert',
  'joachim','jochen','joerg','jörg','josef','julius','jens','kai',
  'killian','kilian','klaas','konrad','kurt','lars','lennart','leopold',
  'lorenz','lothar','ludwig','lutz','manfred','matthias','max','moritz',
  'nikolaus','norbert','oskar','otto','pascal','ralf','raphael','reinhard',
  'roland','roman','rudi','rüdiger','rupert','rutger','samuel','sascha',
  'siegfried','simon','stephan','thorsten','tim','tobias','udo','uwe',
  'valentin','viktor','vincent','volker','willi','willy','wulf','yannick',
]);

// ── Geschlechts-Signalwörter (Deutsch) ──────────────────────────────────────

const FEMALE_SIGNALS = [
  /\b(frau|mme\.?|fräulein)\b/i,
  /\bich bin (die|eine)\b/i,
  /\b(meine tochter|meine schwester|meine mutter|meine freundin|meine kollegin)\b/i,
  /\bals frau\b/i,
  /\b(schwestern|hausfrau|ärztin|lehrerin|sekretärin|chefin|managerin)\b/i,
  /\b(schwanger|schwangerschaft|geburt|entbindung)\b/i,
];

const MALE_SIGNALS = [
  /\b(herr|hr\.?)\b/i,
  /\bich bin (der|ein)\b/i,
  /\b(mein sohn|mein bruder|mein vater|mein freund|mein kollege)\b/i,
  /\bals mann\b/i,
  /\b(herren|hausmann|arzt|lehrer|sekretär|chef|manager)\b/i,
];

// ── Gesprächs-Kontext-Speicher ───────────────────────────────────────────────

const callContexts = new Map();

class GenderDetector {
  /**
   * Geschlecht aus deutschen Text-Signalen erkennen.
   * Gibt { gender: 'female'|'male'|'unknown', confidence: 0–1, signals: [] } zurück.
   */
  detectFromText(text) {
    if (!text) return { gender: 'unknown', confidence: 0, signals: [] };

    const lower = text.toLowerCase();
    const signals = [];
    let femaleScore = 0;
    let maleScore = 0;

    // 1. Anredeformen direkt
    if (/\bfrau\b/.test(lower)) { femaleScore += 3; signals.push('anrede:frau'); }
    if (/\bherr\b/.test(lower))  { maleScore   += 3; signals.push('anrede:herr'); }

    // 2. Signal-Muster prüfen
    for (const pattern of FEMALE_SIGNALS) {
      if (pattern.test(text)) { femaleScore += 2; signals.push(`muster:female`); }
    }
    for (const pattern of MALE_SIGNALS) {
      if (pattern.test(text)) { maleScore += 2; signals.push(`muster:male`); }
    }

    // 3. Vorname erkennen
    const nameResult = this._detectNameFromText(lower);
    if (nameResult.gender === 'female') { femaleScore += nameResult.confidence * 2; signals.push(`name:${nameResult.name}`); }
    if (nameResult.gender === 'male')   { maleScore   += nameResult.confidence * 2; signals.push(`name:${nameResult.name}`); }

    // 4. "Ich heiße / Mein Name ist …"
    const nameIntroPattern = /(?:ich heiße|mein name ist|hier (?:ist|spricht)|mein name|ich bin)\s+([A-ZÄÖÜ][a-zäöüß]+)/i;
    const introMatch = text.match(nameIntroPattern);
    if (introMatch) {
      const detectedName = introMatch[1].toLowerCase();
      if (FEMALE_NAMES.has(detectedName)) { femaleScore += 4; signals.push(`intro_name:female:${introMatch[1]}`); }
      if (MALE_NAMES.has(detectedName))   { maleScore   += 4; signals.push(`intro_name:male:${introMatch[1]}`); }
    }

    const total = femaleScore + maleScore;
    if (total === 0) return { gender: 'unknown', confidence: 0, signals };

    if (femaleScore > maleScore) {
      return { gender: 'female', confidence: Math.min(femaleScore / total, 1), signals };
    } else if (maleScore > femaleScore) {
      return { gender: 'male', confidence: Math.min(maleScore / total, 1), signals };
    }
    return { gender: 'unknown', confidence: 0, signals };
  }

  /**
   * Stimm-Tonhöhe analysieren (Grundfrequenz).
   * Erwartet Float32Array von PCM-Samples (16kHz Mono).
   * Female: ~165–255 Hz | Male: ~85–155 Hz
   */
  detectFromPitch(audioSamples, sampleRate = 16000) {
    const f0 = this._estimatePitch(audioSamples, sampleRate);
    if (!f0) return { gender: 'unknown', confidence: 0, f0: null };

    if (f0 >= 165 && f0 <= 280) return { gender: 'female', confidence: 0.75, f0 };
    if (f0 >= 80  && f0 <= 155) return { gender: 'male',   confidence: 0.75, f0 };
    // Übergangsbereich 155–165 Hz → niedriger Confidence
    if (f0 > 155 && f0 < 165) {
      return { gender: 'female', confidence: 0.45, f0 };
    }
    return { gender: 'unknown', confidence: 0.2, f0 };
  }

  /**
   * Gesprächskontext aktualisieren und bestes Ergebnis ableiten.
   */
  updateAndGetGender(callSid, textResult, pitchResult = null) {
    if (!callContexts.has(callSid)) {
      callContexts.set(callSid, { femaleScore: 0, maleScore: 0, history: [], resolvedGender: null });
    }
    const ctx = callContexts.get(callSid);

    // Wenn bereits sicher → beibehalten
    if (ctx.resolvedGender && ctx.femaleScore > 6 || ctx.maleScore > 6) {
      return ctx.resolvedGender;
    }

    const weight = textResult.confidence || 0;
    if (textResult.gender === 'female') ctx.femaleScore += weight * 2;
    if (textResult.gender === 'male')   ctx.maleScore   += weight * 2;

    if (pitchResult) {
      const pw = (pitchResult.confidence || 0) * 1.5;
      if (pitchResult.gender === 'female') ctx.femaleScore += pw;
      if (pitchResult.gender === 'male')   ctx.maleScore   += pw;
    }

    ctx.history.push({ text: textResult, pitch: pitchResult, ts: Date.now() });

    let gender = 'unknown';
    if (ctx.femaleScore > ctx.maleScore && ctx.femaleScore > 1.5) gender = 'female';
    else if (ctx.maleScore > ctx.femaleScore && ctx.maleScore > 1.5) gender = 'male';

    ctx.resolvedGender = gender;
    return gender;
  }

  getStoredGender(callSid) {
    return callContexts.get(callSid)?.resolvedGender || 'unknown';
  }

  clearCall(callSid) {
    callContexts.delete(callSid);
  }

  /** Anredeform auf Deutsch zurückgeben */
  getGermanSalutation(gender) {
    if (gender === 'female') return 'Frau';
    if (gender === 'male')   return 'Herr';
    return null;
  }

  // ── Private Hilfsmethoden ──────────────────────────────────────────────────

  _detectNameFromText(lower) {
    const words = lower.split(/\s+/);
    for (const word of words) {
      const clean = word.replace(/[^a-zäöüß-]/g, '');
      if (FEMALE_NAMES.has(clean)) return { gender: 'female', name: clean, confidence: 0.9 };
      if (MALE_NAMES.has(clean))   return { gender: 'male',   name: clean, confidence: 0.9 };
    }
    return { gender: 'unknown', name: null, confidence: 0 };
  }

  /** Einfache Autokorrelation zur Grundfrequenzschätzung */
  _estimatePitch(samples, sampleRate) {
    if (!samples || samples.length < 512) return null;

    const minLag = Math.floor(sampleRate / 280); // 280 Hz max
    const maxLag = Math.floor(sampleRate / 80);  // 80 Hz min

    let bestCorr = -Infinity;
    let bestLag = -1;

    const n = Math.min(samples.length, 2048);
    for (let lag = minLag; lag <= maxLag; lag++) {
      let corr = 0;
      for (let i = 0; i < n - lag; i++) {
        corr += samples[i] * samples[i + lag];
      }
      if (corr > bestCorr) {
        bestCorr = corr;
        bestLag = lag;
      }
    }

    if (bestLag < 0 || bestCorr < 0) return null;
    return sampleRate / bestLag;
  }
}

module.exports = new GenderDetector();
