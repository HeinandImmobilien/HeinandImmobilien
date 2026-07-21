# Formulare per E-Mail einrichten (Vercel + Resend)

Alle Anfrageformulare der Website (Leistungsseiten, Standortseiten, Kontakt,
Schadensmeldung) senden ihre Daten an `/api/contact`. Diese Datei liegt unter
`api/contact.js` und läuft als Vercel Serverless Function — sie braucht kein
eigenes Hosting und keine npm-Installation, nur zwei kurze Einrichtungsschritte.

## 1. Resend-Konto anlegen

1. Auf [resend.com](https://resend.com) mit der E-Mail-Adresse registrieren,
   an die die Anfragen später gesendet werden sollen (z. B.
   mail.philipphartung@gmail.com).
2. Im Dashboard unter **API Keys** einen neuen Key erstellen und kopieren.

Ohne eigene verifizierte Domain kann Resend E-Mails nur an die Adresse
senden, mit der das Konto registriert wurde — das reicht hier genau aus, da
die Anfragen ja an dich selbst gehen sollen. Willst du später von einer
eigenen Adresse wie `anfrage@heinand.de` aus senden, muss die Domain heinand.de
zusätzlich bei Resend verifiziert werden (DNS-Einträge, in Resend unter
**Domains**).

## 2. Umgebungsvariable in Vercel setzen

1. Projekt in Vercel öffnen → **Settings → Environment Variables**.
2. Variable hinzufügen:
   - Name: `RESEND_API_KEY`
   - Wert: der eben kopierte API-Key
3. Optional: eine zweite Variable `NOTIFY_EMAIL`, falls die Anfragen an eine
   andere Adresse als mail.philipphartung@gmail.com gehen sollen.
4. Deployment neu ausführen (Redeploy), damit die Variable aktiv wird.

## Das war's

Sobald das Deployment läuft, landet jede Formular-Anfrage als E-Mail im
angegebenen Postfach — mit allen ausgefüllten Feldern und dem jeweiligen
Formularnamen (z. B. "Mietverwaltung — Angebotsanfrage" oder
"Schadensmeldung") in der Betreffzeile. Antwortest du direkt auf die E-Mail,
geht die Antwort automatisch an die vom Absender eingetragene E-Mail-Adresse.

Ein verstecktes Feld pro Formular blockt außerdem automatisierte
Bot-Einsendungen ab (kein zusätzlicher Aufwand für dich).

## Fotos bei der Schadensmeldung

Im Schadensmeldungsformular können Kunden bis zu 5 Fotos hochladen. Die
Bilder werden im Browser automatisch verkleinert (max. 1600px Kante, JPEG)
und der E-Mail als Anhang beigefügt — dafür ist keine zusätzliche
Konfiguration nötig, das läuft über denselben Resend-Versand. Einzelne, sehr
große Fotos werden automatisch übersprungen (mit Hinweis in der E-Mail),
damit die Anfrage nicht an Größenlimits scheitert.

## Ortssuche mit Live-Entfernung

Die Ortssuche auf der Startseite ("Sind wir auch in Ihrem Ort tätig?") kennt
eine feste Liste von rund 90 Orten in der Region mit hinterlegter Entfernung.
Gibt jemand einen Ort ein, der nicht in dieser Liste steht (z. B. München),
wird automatisch `api/distance.js` aufgerufen: Diese Funktion ermittelt die
Koordinaten des Ortes über die kostenlose OpenStreetMap-Geokodierung
(Nominatim) und berechnet die Luftlinien-Entfernung zu Mainz. So bekommt
praktisch jeder Ort in Deutschland eine echte km-Angabe und die passende
Meldung ("innerhalb" bzw. "außerhalb unseres Einsatzgebiets") — statt
generisch "nicht gefunden". Auch das braucht keine zusätzliche Einrichtung
oder API-Key, läuft direkt mit.

## Ohne Vercel testen

Lokal lässt sich die Funktion mit der Vercel-CLI testen:

```
npm i -g vercel
vercel dev
```

Damit läuft die Seite inklusive `/api/contact` lokal unter `localhost:3000`.
