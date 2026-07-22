// HEINAND Immobilien — Frontend-Maske
// Alle Formulare sind reine Masken: es findet noch keine echte Übermittlung statt.

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initMegaMenu();
  initFaq();
  initCookieBanner();
  initContactForms();
  markActiveNav();
  initLeafletMaps();
  initLocationSearch();
  initContactTabs();
  initSchadensPriority();
});

function initSchadensPriority() {
  const select = document.getElementById('schadensart');
  const box = document.getElementById('priorityIndicator');
  if (!select || !box) return;
  const titleEl = document.getElementById('priorityTitle');
  const descEl = document.getElementById('priorityDesc');
  const impactEl = document.getElementById('priorityImpact');

  const COPY = {
    akut: {
      title: 'Akut / Gefahr',
      desc: 'Sofortiger Handlungsbedarf.',
      impact: '→ Sofortige Reaktion — rufen Sie uns zusätzlich telefonisch an!',
    },
    dringend: {
      title: 'Dringend',
      desc: 'Beeinträchtigt den Alltag spürbar.',
      impact: '→ Zeitnahe Koordination, in der Regel innerhalb von 24 Stunden.',
    },
    regulaer: {
      title: 'Regulär',
      desc: 'Kein akuter Zeitdruck.',
      impact: '→ Bearbeitung innerhalb weniger Werktage.',
    },
    unbekannt: {
      title: 'Wird nach Ihrer Beschreibung eingestuft',
      desc: 'Bitte beschreiben Sie den Schaden unten so genau wie möglich.',
      impact: '→ Bei akuter Gefahr rufen Sie uns bitte zusätzlich direkt an.',
    },
  };

  select.addEventListener('change', () => {
    const opt = select.options[select.selectedIndex];
    const priority = opt ? opt.dataset.priority : null;
    const copy = COPY[priority];
    if (!copy) { box.hidden = true; return; }
    box.hidden = false;
    box.className = 'priority-indicator ' + priority;
    titleEl.textContent = copy.title;
    descEl.textContent = copy.desc;
    impactEl.textContent = copy.impact;
  });
}

function initContactTabs() {
  const wrap = document.querySelector('.contact-tabs');
  if (!wrap) return;
  const btns = wrap.querySelectorAll('.tab-btn');
  const panels = wrap.querySelectorAll('.tab-panel');

  const activate = (tab) => {
    btns.forEach(b => {
      const isActive = b.dataset.tab === tab;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });
    panels.forEach(p => p.classList.toggle('active', p.dataset.tabPanel === tab));
  };

  btns.forEach(btn => btn.addEventListener('click', () => activate(btn.dataset.tab)));

  // Direkt zum Buchungs-Tab springen, wenn die Seite mit #termin aufgerufen wird
  // (z. B. über "Direkt Termin buchen" von anderen Seiten).
  if (window.location.hash === '#termin') {
    activate('booking');
  }
}

function initLeafletMaps() {
  document.querySelectorAll('.leaflet-map').forEach(el => {
    if (typeof L === 'undefined') return;
    let points = [];
    let radiusKm = 50;
    try { points = JSON.parse(el.dataset.points || '[]'); } catch (e) { points = []; }
    if (el.dataset.radiusKm) radiusKm = parseFloat(el.dataset.radiusKm);

    const main = points.find(p => p.main) || points[0];
    if (!main) return;

    const map = L.map(el, {
      scrollWheelZoom: false,
      center: [main.lat, main.lon],
      zoom: 9,
    });

    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap, &copy; CARTO',
      maxZoom: 19,
      subdomains: 'abcd',
    }).addTo(map);

    // 50-km-Einzugsgebiet als Kreis
    L.circle([main.lat, main.lon], {
      radius: radiusKm * 1000,
      color: '#9f7e3e',
      weight: 1.5,
      fillColor: '#9f7e3e',
      fillOpacity: 0.06,
      dashArray: '4 6',
    }).addTo(map);

    points.forEach(p => {
      const marker = L.circleMarker([p.lat, p.lon], {
        radius: p.main ? 7 : 5,
        color: p.main ? '#9f7e3e' : '#0f3063',
        weight: 2,
        fillColor: p.main ? '#9f7e3e' : '#ffffff',
        fillOpacity: 1,
      }).addTo(map);
      const label = p.main
        ? `<strong>${p.name}</strong><span>Firmensitz</span>`
        : `<strong>${p.name}</strong><span>ca. ${p.dist} km von Mainz</span>`;
      marker.bindTooltip(label, { direction: 'top', offset: [0, -6], className: 'hn-map-tooltip' });
    });

    // Kartenausschnitt an alle Punkte + Radius anpassen
    const bounds = L.latLngBounds(points.map(p => [p.lat, p.lon]));
    map.fitBounds(bounds.pad(0.25));

    map.on('focus', () => map.scrollWheelZoom.enable());
    map.on('blur', () => map.scrollWheelZoom.disable());
  });
}

function initMobileNav() {
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.querySelector('.mobile-nav');
  const closeBtn = document.querySelector('.mobile-nav-close');
  if (!toggle || !panel) return;
  toggle.addEventListener('click', () => panel.classList.add('open'));
  if (closeBtn) closeBtn.addEventListener('click', () => panel.classList.remove('open'));
  panel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => panel.classList.remove('open')));
}

function initMegaMenu() {
  const trigger = document.querySelector('.nav-dropdown-trigger');
  const menu = document.querySelector('.mega-menu');
  if (!trigger || !menu) return;
  const close = () => menu.classList.remove('open');
  trigger.addEventListener('click', (e) => {
    e.stopPropagation();
    menu.classList.toggle('open');
  });
  document.addEventListener('click', (e) => {
    if (!menu.contains(e.target) && e.target !== trigger) close();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
}

function initFaq() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });
}

function initCookieBanner() {
  const banner = document.querySelector('.cookie-banner');
  if (!banner) return;
  const KEY = 'hn_cookie_consent';
  const stored = localStorage.getItem(KEY);
  if (!stored) {
    setTimeout(() => banner.classList.add('open'), 600);
  }
  banner.querySelectorAll('[data-cookie-action]').forEach(btn => {
    btn.addEventListener('click', () => {
      localStorage.setItem(KEY, btn.dataset.cookieAction);
      banner.classList.remove('open');
    });
  });
  document.querySelectorAll('[data-open-cookie-settings]').forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      banner.classList.add('open');
    });
  });
}

// Verkleinert ein hochgeladenes Foto clientseitig (max. 1600px Kante,
// JPEG-Qualität ~72%), damit die E-Mail-Anfrage klein genug für den Versand
// bleibt. Gibt bei Fehlern (z. B. nicht unterstütztes Dateiformat) null
// zurück, statt die ganze Anfrage zu blockieren.
function resizeImageForUpload(file, maxDim, quality) {
  maxDim = maxDim || 1600;
  quality = quality || 0.72;
  return new Promise((resolve) => {
    if (!file || !file.type || file.type.indexOf('image/') !== 0) { resolve(null); return; }
    const reader = new FileReader();
    reader.onerror = () => resolve(null);
    reader.onload = () => {
      const img = new Image();
      img.onerror = () => resolve(null);
      img.onload = () => {
        let width = img.naturalWidth;
        let height = img.naturalHeight;
        if (!width || !height) { resolve(null); return; }
        if (width > maxDim || height > maxDim) {
          const scale = maxDim / Math.max(width, height);
          width = Math.round(width * scale);
          height = Math.round(height * scale);
        }
        const canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0, width, height);
        let dataUrl;
        try { dataUrl = canvas.toDataURL('image/jpeg', quality); }
        catch (e) { resolve(null); return; }
        const base64 = dataUrl.split(',')[1];
        if (!base64) { resolve(null); return; }
        const baseName = (file.name || 'foto').replace(/\.[^.]+$/, '');
        resolve({ filename: baseName + '.jpg', content: base64 });
      };
      img.src = reader.result;
    };
    reader.readAsDataURL(file);
  });
}

function initContactForms() {
  document.querySelectorAll('form[data-contact-form]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      const original = btn ? btn.textContent : '';

      let note = form.querySelector('.form-mock-note');
      if (!note) {
        note = document.createElement('p');
        note.className = 'form-mock-note';
        form.appendChild(note);
      }

      // Spamschutz: Wenn das versteckte Honeypot-Feld befüllt ist, brechen wir
      // still ab (typisches Bot-Verhalten), ohne dass der Nutzer etwas merkt.
      const hp = form.querySelector('input[name="_gotcha"]');
      if (hp && hp.value) return;

      // Formularfelder anhand ihrer sichtbaren Labels einsammeln, damit die
      // E-Mail lesbare deutsche Feldnamen enthält. Datei-Felder (Fotos)
      // werden separat verarbeitet, nicht als Text übernommen.
      const felder = {};
      form.querySelectorAll('.form-field').forEach(field => {
        const label = field.querySelector('label');
        const input = field.querySelector('input, select, textarea');
        if (!label || !input || input.type === 'file') return;
        const key = label.textContent.replace(/\s*\*$/, '').trim();
        felder[key] = input.value;
      });

      // Fotos (falls vorhanden): clientseitig verkleinern, damit die Anfrage
      // klein genug für den Versand per E-Mail bleibt.
      const fileInput = form.querySelector('input[type="file"]');
      let anhaenge = [];
      if (fileInput && fileInput.files && fileInput.files.length) {
        if (btn) btn.textContent = 'Fotos werden vorbereitet …';
        const files = Array.from(fileInput.files).slice(0, 5);
        const results = await Promise.all(files.map(f => resizeImageForUpload(f)));
        anhaenge = results.filter(Boolean);
      }

      if (btn) { btn.disabled = true; btn.textContent = 'Wird gesendet …'; }

      try {
        const res = await fetch('/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            formular: form.dataset.formName || 'Anfrage über heinand.de',
            felder,
            gotcha: hp ? hp.value : '',
            anhaenge,
          }),
        });
        if (!res.ok) throw new Error('Serverfehler ' + res.status);

        note.style.cssText = 'margin-top:14px;font-size:13px;color:#1b3f7a;background:#eef1f6;padding:12px 14px;border-radius:10px;';
        note.textContent = 'Danke — Ihre Anfrage wurde erfolgreich versendet. Wir melden uns in Kürze.';
        form.reset();
        if (btn) btn.textContent = 'Danke — gesendet';
      } catch (err) {
        note.style.cssText = 'margin-top:14px;font-size:13px;color:#b3441f;background:#fbeae4;padding:12px 14px;border-radius:10px;';
        note.textContent = 'Da ist leider etwas schiefgelaufen. Bitte versuchen Sie es erneut oder kontaktieren Sie uns telefonisch.';
        if (btn) btn.textContent = original;
      } finally {
        if (btn) {
          setTimeout(() => {
            btn.disabled = false;
            if (btn.textContent.indexOf('gesendet') === -1) btn.textContent = original;
          }, 3000);
        }
      }
    });
  });
}

function markActiveNav() {
  const path = window.location.pathname.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
  document.querySelectorAll('.main-nav a, .mobile-nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (!href) return;
    const normalized = href.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
    if (normalized !== '' && normalized !== '/' && path.endsWith(normalized)) {
      a.classList.add('active');
    }
  });
}

function normalizeOrt(s) {
  return s
    .toLowerCase()
    .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

function initLocationSearch() {
  document.querySelectorAll('.location-search').forEach(widget => {
    const input = widget.querySelector('.location-search-input');
    const searchBtn = widget.querySelector('.location-search-btn');
    const suggestBox = widget.querySelector('.location-search-suggestions');
    const resultBox = widget.querySelector('.location-search-result');
    const dataScript = widget.querySelector('.location-search-data');
    if (!input || !dataScript) return;

    let data = [];
    try { data = JSON.parse(dataScript.textContent); } catch (e) { data = []; }
    const radius = parseInt(widget.dataset.radius, 10) || 50;

    const closeSuggestions = () => { suggestBox.classList.remove('open'); suggestBox.innerHTML = ''; };

    const showLoading = () => {
      resultBox.classList.remove('ok', 'no', 'unknown');
      resultBox.innerHTML = '<strong>Einen Moment …</strong>Wir ermitteln die Entfernung zu diesem Ort.';
      resultBox.classList.add('unknown', 'visible');
    };

    const showResult = (loc) => {
      resultBox.classList.remove('ok', 'no', 'unknown');
      if (!loc) {
        resultBox.innerHTML = '<strong>Ort nicht gefunden.</strong>Wir konnten diesen Ort nicht eindeutig finden — <a href="kontakt.html">kontaktieren Sie uns</a>, wir sagen Ihnen gerne, ob wir dort tätig sind.';
        resultBox.classList.add('unknown', 'visible');
        return;
      }
      const zusatz = loc.live ? ' Luftlinie (automatisch berechnet)' : '';
      if (loc.core) {
        resultBox.innerHTML = `<strong>&#10003; Ja, wir sind in ${loc.name} tätig.</strong>Ca. ${loc.distance} km${zusatz} von unserem Sitz in Mainz entfernt — als feste Standort-Region gehört ${loc.name} zu unserem Einzugsgebiet.`;
        resultBox.classList.add('ok', 'visible');
      } else if (loc.distance <= radius) {
        resultBox.innerHTML = `<strong>&#10003; Ja, wir sind in ${loc.name} tätig.</strong>Ca. ${loc.distance} km${zusatz} von unserem Sitz in Mainz entfernt — innerhalb unseres Einsatzgebiets.`;
        resultBox.classList.add('ok', 'visible');
      } else {
        resultBox.innerHTML = `<strong>&#10007; ${loc.name} liegt leider außerhalb unseres Einsatzgebiets.</strong>Ca. ${loc.distance} km${zusatz} von Mainz entfernt — das ist uns für die von uns angestrebte Servicequalität zu weit. <a href="kontakt.html">Sprechen Sie uns dennoch an</a>, im Einzelfall besprechen wir Alternativen.`;
        resultBox.classList.add('no', 'visible');
      }
    };

    const renderSuggestions = (matches, query) => {
      if (!matches.length) { closeSuggestions(); return; }
      suggestBox.innerHTML = matches.slice(0, 8).map(loc =>
        `<button type="button" data-name="${loc.name}"><span>${loc.name}</span><span class="note">${loc.note || ''}</span></button>`
      ).join('');
      suggestBox.classList.add('open');
      suggestBox.querySelectorAll('button').forEach(btn => {
        btn.addEventListener('click', () => {
          input.value = btn.dataset.name;
          closeSuggestions();
          const found = data.find(l => l.name === btn.dataset.name);
          showResult(found);
        });
      });
    };

    input.addEventListener('input', () => {
      const q = normalizeOrt(input.value);
      resultBox.classList.remove('visible');
      if (q.length < 2) { closeSuggestions(); return; }
      const matches = data.filter(loc => normalizeOrt(loc.name).includes(q));
      renderSuggestions(matches, q);
    });

    const runSearch = async () => {
      const rawValue = input.value.trim();
      const q = normalizeOrt(rawValue);
      if (!q) { input.focus(); return; }
      closeSuggestions();

      const exact = data.find(loc => normalizeOrt(loc.name) === q);
      const partial = exact || data.find(loc => normalizeOrt(loc.name).includes(q));
      if (partial) { showResult(partial); return; }

      // Kein Treffer in unserer festen Orte-Liste: Entfernung live über die
      // Geokodierungs-API abfragen, statt "nicht gefunden" zu melden. So
      // bekommt jeder Ort in Deutschland eine echte km-Angabe.
      showLoading();
      try {
        const res = await fetch('/api/distance?ort=' + encodeURIComponent(rawValue));
        if (!res.ok) { showResult(null); return; }
        const found = await res.json();
        if (!found || typeof found.distance !== 'number') { showResult(null); return; }
        showResult({ name: found.name || rawValue, distance: found.distance, core: false, live: true });
      } catch (err) {
        showResult(null);
      }
    };

    input.addEventListener('keydown', (e) => {
      if (e.key !== 'Enter') return;
      e.preventDefault();
      runSearch();
    });

    if (searchBtn) searchBtn.addEventListener('click', runSearch);

    document.addEventListener('click', (e) => {
      if (!widget.contains(e.target)) closeSuggestions();
    });
  });
}
