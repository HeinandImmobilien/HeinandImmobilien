// api/contact.js
//
// Vercel Serverless Function: nimmt Formular-Anfragen von heinand.de entgegen
// und sendet eine Benachrichtigungs-E-Mail per Resend (https://resend.com).
//
// Benötigte Umgebungsvariable (in den Vercel-Projekteinstellungen anlegen):
//   RESEND_API_KEY   — API-Key aus dem Resend-Dashboard
// Optional:
//   NOTIFY_EMAIL     — Empfänger-Adresse, Standard: mail.philipphartung@gmail.com
//
// Kein npm-Paket nötig — der Aufruf läuft über die in Node eingebaute fetch-API.

const NOTIFY_EMAIL = process.env.NOTIFY_EMAIL || 'mail.philipphartung@gmail.com';
// Absenderadresse über die Resend-Testdomain. Funktioniert ohne eigene
// Domain-Verifizierung, solange NOTIFY_EMAIL die Adresse ist, mit der das
// Resend-Konto erstellt wurde. Mit eigener verifizierter Domain kann hier
// z. B. "HEINAND Immobilien <anfrage@heinand.de>" eingetragen werden.
const FROM_EMAIL = 'HEINAND Website <onboarding@resend.dev>';

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = {}; }
  }
  body = body || {};

  // Honeypot: Ein verstecktes Feld, das nur Bots ausfüllen. Ist es befüllt,
  // brechen wir "erfolgreich" ab, ohne eine E-Mail zu senden.
  if (body.gotcha) {
    res.status(200).json({ ok: true });
    return;
  }

  const formular = (body.formular || 'Anfrage über heinand.de').toString().slice(0, 200);
  const felder = body.felder && typeof body.felder === 'object' ? body.felder : {};
  const entries = Object.entries(felder).filter(([, v]) => v !== undefined && v !== null && String(v).trim() !== '');

  if (entries.length === 0) {
    res.status(400).json({ error: 'Keine Formulardaten übermittelt.' });
    return;
  }

  // Foto-Anhänge (bereits clientseitig verkleinert): auf max. 5 Dateien und
  // ~6 MB pro Base64-Anhang begrenzen, damit die Anfrage nicht an
  // Größenlimits scheitert. Überzählige/zu große Anhänge werden stillschweigend
  // verworfen, die restliche Anfrage wird trotzdem gesendet.
  const rawAnhaenge = Array.isArray(body.anhaenge) ? body.anhaenge : [];
  const MAX_ATTACHMENTS = 5;
  const MAX_BASE64_LEN = 8_000_000; // ~6 MB dekodiert
  const attachments = rawAnhaenge
    .filter(a => a && typeof a.content === 'string' && typeof a.filename === 'string')
    .filter(a => a.content.length <= MAX_BASE64_LEN)
    .slice(0, MAX_ATTACHMENTS)
    .map(a => ({ filename: a.filename.slice(0, 120), content: a.content }));
  const skippedAttachments = rawAnhaenge.length - attachments.length;

  // Antwort-Adresse automatisch erkennen: die erste Eingabe, die wie eine
  // E-Mail-Adresse aussieht, wird als Reply-To gesetzt — so kann direkt aus
  // dem Postfach heraus geantwortet werden.
  let replyTo;
  for (const [, value] of entries) {
    const v = String(value).trim();
    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) { replyTo = v; break; }
  }

  const rowsHtml = entries.map(([label, value]) => (
    `<tr>` +
    `<td style="padding:6px 12px;color:#5b6472;font-size:13px;vertical-align:top;white-space:nowrap;">${escapeHtml(label)}</td>` +
    `<td style="padding:6px 12px;font-size:14px;color:#172136;">${escapeHtml(String(value)).replace(/\n/g, '<br>')}</td>` +
    `</tr>`
  )).join('');

  const attachmentNoteHtml = attachments.length
    ? `<p style="color:#5b6472;font-size:13px;">${attachments.length} Foto(s) angehängt.${skippedAttachments > 0 ? ` (${skippedAttachments} weitere(s) Foto konnte wegen Dateigröße nicht mitgesendet werden.)` : ''}</p>`
    : (skippedAttachments > 0 ? `<p style="color:#b3441f;font-size:13px;">${skippedAttachments} Foto(s) konnten wegen Dateigröße nicht mitgesendet werden.</p>` : '');

  const html = `
    <div style="font-family:Arial,Helvetica,sans-serif;max-width:600px;margin:0 auto;">
      <h2 style="color:#0f3063;margin-bottom:4px;">Neue Anfrage</h2>
      <p style="color:#9f7e3e;font-weight:bold;margin-top:0;">${escapeHtml(formular)}</p>
      <table style="border-collapse:collapse;width:100%;">${rowsHtml}</table>
      ${attachmentNoteHtml}
      <p style="color:#8a92a3;font-size:12px;margin-top:24px;">Gesendet über das Formular „${escapeHtml(formular)}“ auf heinand.de.</p>
    </div>`;

  const text = `Neue Anfrage: ${formular}\n\n` +
    entries.map(([label, value]) => `${label}: ${value}`).join('\n') +
    (attachments.length ? `\n\n${attachments.length} Foto(s) angehängt.` : '') +
    (skippedAttachments > 0 ? `\n${skippedAttachments} Foto(s) konnten wegen Dateigröße nicht mitgesendet werden.` : '');

  if (!process.env.RESEND_API_KEY) {
    console.error('RESEND_API_KEY ist nicht gesetzt — siehe Kommentar am Dateianfang von api/contact.js.');
    res.status(500).json({ error: 'E-Mail-Versand ist noch nicht konfiguriert.' });
    return;
  }

  try {
    const payload = {
      from: FROM_EMAIL,
      to: [NOTIFY_EMAIL],
      subject: `Neue Anfrage: ${formular}`,
      html,
      text,
    };
    if (replyTo) payload.reply_to = replyTo;
    if (attachments.length) payload.attachments = attachments;

    const resendRes = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!resendRes.ok) {
      const errText = await resendRes.text();
      console.error('Resend-Fehler:', resendRes.status, errText);
      res.status(502).json({ error: 'E-Mail konnte nicht gesendet werden.' });
      return;
    }

    res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Unerwarteter Fehler beim E-Mail-Versand:', err);
    res.status(500).json({ error: 'Unerwarteter Fehler.' });
  }
};
