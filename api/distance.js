// api/distance.js
//
// GET /api/distance?ort=<Ortsname>
//
// Wird von der Ortssuche auf der Website genutzt, wenn ein eingegebener Ort
// nicht in unserer festen Orte-Liste (components.py: SEARCH_LOCATIONS) steht.
// Statt "Ort nicht gefunden" zu melden, geokodiert diese Funktion den Ort
// über die öffentliche Nominatim-API (OpenStreetMap) und berechnet die
// Luftlinien-Entfernung zu unserem Standort in Mainz — für praktisch jeden
// Ort in Deutschland.
//
// Kein npm-Paket nötig (nutzt die in Node eingebaute fetch-API). Keine
// Umgebungsvariable erforderlich — Nominatim ist ohne API-Key nutzbar,
// solange die Nutzungsrichtlinien eingehalten werden (max. 1 Anfrage/Sek.,
// aussagekräftiger User-Agent). Für unser Nutzungsvolumen (gelegentliche
// Suchen einzelner Website-Besucher) ist das unproblematisch.

const OFFICE = { lat: 49.9929, lon: 8.2473 }; // HEINAND Immobilien, Menimaneweg 4, Mainz (Zentrum, Näherung)

function haversineKm(lat1, lon1, lat2, lon2) {
  const R = 6371;
  const toRad = (d) => (d * Math.PI) / 180;
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const ort = (req.query.ort || '').toString().trim().slice(0, 100);
  if (!ort) {
    res.status(400).json({ error: 'Kein Ort angegeben.' });
    return;
  }

  try {
    const url =
      'https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=de&addressdetails=0&q=' +
      encodeURIComponent(ort);

    const geoRes = await fetch(url, {
      headers: {
        // Nominatim verlangt einen aussagekräftigen User-Agent statt des
        // generischen Standard-Headers.
        'User-Agent': 'heinand-immobilien-website/1.0 (+https://www.heinand.de; mail.philipphartung@gmail.com)',
        'Accept-Language': 'de',
      },
    });

    if (!geoRes.ok) {
      res.status(502).json({ error: 'Geokodierung fehlgeschlagen.' });
      return;
    }

    const results = await geoRes.json();
    if (!Array.isArray(results) || results.length === 0) {
      res.status(404).json({ error: 'Ort nicht gefunden.' });
      return;
    }

    const place = results[0];
    const lat = parseFloat(place.lat);
    const lon = parseFloat(place.lon);
    if (Number.isNaN(lat) || Number.isNaN(lon)) {
      res.status(404).json({ error: 'Ort nicht gefunden.' });
      return;
    }

    const distance = Math.round(haversineKm(OFFICE.lat, OFFICE.lon, lat, lon));
    // Nur den ersten Teil des Nominatim-Namens verwenden (Ortsname ohne
    // vollständige Adresse/Landkreis-Anhängsel).
    const name = place.display_name ? place.display_name.split(',')[0].trim() : ort;

    res.status(200).json({ name, distance });
  } catch (err) {
    console.error('Fehler bei Geokodierung/Distanzberechnung:', err);
    res.status(500).json({ error: 'Unerwarteter Fehler.' });
  }
};
