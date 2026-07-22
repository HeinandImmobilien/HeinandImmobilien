#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die HEINAND-Immobilien Frontend-Maske.
Erzeugt statische HTML-Dateien aus wiederverwendbaren Bausteinen
(Header, Mega-Menü, Footer, Cookie-Banner, CTA-Banner) + Seiteninhalten.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PHONE = "06131 - 6248240"
PHONE_TEL = "tel:+4961316248240"
EMAIL = "info@heinand.de"

# --------------------------------------------------------------------------
# Icon / Logo SVG (Nachbau des Original-Icons: zwei stilisierte Giebeldächer)
# --------------------------------------------------------------------------

def mark_svg(color="currentColor", size=40):
    return f'''<svg viewBox="0 0 48 48" width="{size}" height="{size}" fill="none" xmlns="http://www.w3.org/2000/svg" style="color:{color}">
<path d="M4 23L14 11L24 23" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 21V39H21V21" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M22 29L30 19L38 29" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M25 27V39H41V27" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="12.5" y="31" width="4" height="8" fill="currentColor"/>
<rect x="30.5" y="33" width="4" height="6" fill="currentColor"/>
</svg>'''

def logo_block(prefix, variant="light", loading="lazy"):
    """variant: 'light' = Logo (blau/gold) für helle Flächen, 'dark' = Logo (weiß/gold) für dunkle Flächen (Footer).
    loading: 'eager' für das Logo im sichtbaren Header (above the fold), sonst 'lazy'
    (Mobile-Nav-Logo ist beim Laden unsichtbar, Footer-Logo liegt unterhalb des Folds)."""
    file = "logo-blue-gold.png" if variant == "light" else "logo-white-gold.png"
    return f'''<a href="{prefix}index.html" class="logo" aria-label="HEINAND Immobilien: Startseite">
      <img src="{prefix}assets/{file}" alt="HEINAND Immobilien" class="logo-img" loading="{loading}">
    </a>'''

def mark_img(prefix, variant="gold", size=64, loading="lazy"):
    """Icon-only Logo (ohne Schriftzug). variant: gold | blue | white. Wird nur
    unterhalb des Folds verwendet (CTA-Band etc.), daher standardmäßig lazy."""
    return f'<img src="{prefix}assets/mark-{variant}.png" alt="" width="{size}" height="{size}" class="mark-img" loading="{loading}">'

# --------------------------------------------------------------------------
# Navigation data
# --------------------------------------------------------------------------

SERVICES_VERWALTUNG = [
    ("Mietverwaltung", "leistungen/mietverwaltung.html", "Komplette Betreuung Ihrer Mietobjekte: von der Korrespondenz bis zur Abrechnung."),
    ("WEG-Verwaltung", "leistungen/weg-verwaltung.html", "Verwaltung für Wohnungseigentümergemeinschaften: rechtssicher und transparent."),
    ("Sondereigentumsverwaltung", "leistungen/se-verwaltung.html", "Betreuung Ihrer Eigentumswohnung innerhalb der WEG: speziell für Kapitalanleger."),
    ("Werterhalt & Instandhaltung", "leistungen/werterhalt-instandhaltung.html", "Regelmäßige Betreuung und schnelle Reaktion: damit Ihr Objekt wertstabil bleibt."),
]
SERVICES_VERKAUF = [
    ("Immobilienverkauf", "leistungen/immobilienverkauf.html", "Vom Exposé bis zum Notartermin: Verkauf mit regionaler Marktkenntnis."),
    ("Immobilienbewertung", "leistungen/immobilienbewertung.html", "Fundierte Werteinschätzung für Verkauf, Vermietung oder Vermögensübersicht."),
]

FOOTER_LEISTUNGEN = SERVICES_VERWALTUNG[:3] + [SERVICES_VERWALTUNG[3]] + SERVICES_VERKAUF
FOOTER_LEISTUNGEN = [
    ("Mietverwaltung", "leistungen/mietverwaltung.html"),
    ("WEG-Verwaltung", "leistungen/weg-verwaltung.html"),
    ("Sondereigentumsverwaltung", "leistungen/se-verwaltung.html"),
    ("Immobilienverkauf", "leistungen/immobilienverkauf.html"),
    ("Immobilienbewertung", "leistungen/immobilienbewertung.html"),
    ("Werterhalt & Instandhaltung", "leistungen/werterhalt-instandhaltung.html"),
]
FOOTER_UNTERNEHMEN = [
    ("Über uns", "ueber-uns.html"),
    ("Unsere Region", "region.html"),
    ("Ratgeber", "blog/index.html"),
    ("Schaden melden", "schadensmeldung.html"),
    ("Kontakt", "kontakt.html"),
]

# --------------------------------------------------------------------------
# Standorte / Einzugsgebiet: Orte im 35-km-Radius um Mainz (Bad Kreuznach
# bleibt als feste Standort-Region unabhängig vom Radius Teil des Gebiets)
# (Distanzen sind gerundete Luftlinien-Näherungen zur Einordnung, keine
# amtlichen Angaben. tier=1 -> eigene Standort-Landingpage, tier=2 -> nur
# Nennung in Liste/Karte.)
# --------------------------------------------------------------------------

LOCATIONS = [
    dict(name="Wiesbaden", slug="wiesbaden", distance=10, bearing=330, tier=1,
         blurb="Die hessische Landeshauptstadt liegt direkt gegenüber von Mainz am anderen Rheinufer: für uns nur eine kurze Fahrt über die Brücke."),
    dict(name="Ingelheim am Rhein", slug="ingelheim", distance=15, bearing=260, tier=1,
         blurb="Weinstadt und Wirtschaftsstandort westlich von Mainz, geprägt von gewachsenen Wohnlagen und soliden Mehrfamilienhäusern."),
    dict(name="Bingen am Rhein", slug="bingen", distance=30, bearing=278, tier=1,
         blurb="Das Tor zum UNESCO-Welterbe Oberes Mittelrheintal: mit historischer Bausubstanz und stabiler Vermietungsnachfrage."),
    dict(name="Alzey", slug="alzey", distance=30, bearing=205, tier=1,
         blurb="Kreisstadt in Rheinhessen mit ruhigem Immobilienmarkt und vielen Ein- und Mehrfamilienhäusern in Eigentümerhand."),
    dict(name="Bad Kreuznach", slug="bad-kreuznach", distance=40, bearing=235, tier=1,
         blurb="Kreisstadt an der Nahe mit historischer Altstadt und wachsendem Bedarf an professioneller Hausverwaltung."),
    dict(name="Rüsselsheim am Main", slug="ruesselsheim", distance=20, bearing=95, tier=1,
         blurb="Industriestadt am Main im Rhein-Main-Gebiet mit hoher Mieternachfrage und viel Mehrfamilienhausbestand."),
    dict(name="Nieder-Olm", slug="nieder-olm", distance=10, bearing=200, tier=1,
         blurb="Verbandsgemeinde direkt südlich von Mainz: beliebte Wohnlage mit kurzen Wegen zu uns."),
    dict(name="Frankfurt am Main", distance=35, bearing=78, tier=2),
    dict(name="Darmstadt", distance=35, bearing=122, tier=2),
    dict(name="Offenbach am Main", distance=40, bearing=82, tier=2),
    dict(name="Groß-Gerau", distance=25, bearing=100, tier=2),
    dict(name="Rüdesheim am Rhein", distance=35, bearing=290, tier=2),
    dict(name="Eltville am Rhein", distance=20, bearing=310, tier=2),
    dict(name="Oestrich-Winkel", distance=25, bearing=298, tier=2),
    dict(name="Geisenheim", distance=30, bearing=292, tier=2),
    dict(name="Idstein", distance=30, bearing=15, tier=2),
    dict(name="Taunusstein", distance=20, bearing=350, tier=2),
    dict(name="Hofheim am Taunus", distance=25, bearing=48, tier=2),
    dict(name="Bad Homburg vor der Höhe", distance=45, bearing=55, tier=2),
    dict(name="Oppenheim", distance=20, bearing=185, tier=2),
    dict(name="Nierstein", distance=15, bearing=180, tier=2),
    dict(name="Nackenheim", distance=13, bearing=180, tier=2),
    dict(name="Bodenheim", distance=10, bearing=185, tier=2),
    dict(name="Gau-Algesheim", distance=20, bearing=265, tier=2),
    dict(name="Budenheim", distance=8, bearing=300, tier=2),
    dict(name="Heidesheim am Rhein", distance=12, bearing=270, tier=2),
    dict(name="Ginsheim-Gustavsburg", distance=15, bearing=80, tier=2),
]

# --------------------------------------------------------------------------
# Ortssuche: große Datenbank für die "Sind Sie auch in ... tätig?"-Suche.
# Distanzen sind gerundete Luftlinien-Näherungen ab Mainz-Zentrum, keine
# amtlichen Angaben. RADIUS_KM ist die Grenze unseres Einsatzgebiets.
# --------------------------------------------------------------------------

RADIUS_KM = 35

# Feste Standort-Regionen, die trotz etwas größerer Entfernung fest zu unserem
# Servicegebiet gehören (eigene Standort-Landingpage, siehe LOCATIONS oben) und
# in der Ortssuche deshalb unabhängig von RADIUS_KM immer als "tätig" gelten.
ALWAYS_SERVED = {"Bad Kreuznach"}

SEARCH_LOCATIONS = [
    # Mainz: Stadtteile
    ("Mainz-Altstadt", 1, "Stadtteil von Mainz"),
    ("Mainz-Neustadt", 2, "Stadtteil von Mainz"),
    ("Mainz-Oberstadt", 2, "Stadtteil von Mainz"),
    ("Mainz-Hartenberg-Münchfeld", 3, "Stadtteil von Mainz"),
    ("Mainz-Bretzenheim", 4, "Stadtteil von Mainz"),
    ("Mainz-Marienborn", 5, "Stadtteil von Mainz"),
    ("Mainz-Lerchenberg", 6, "Stadtteil von Mainz"),
    ("Mainz-Drais", 6, "Stadtteil von Mainz"),
    ("Mainz-Finthen", 8, "Stadtteil von Mainz"),
    ("Mainz-Gonsenheim", 5, "Stadtteil von Mainz"),
    ("Mainz-Mombach", 4, "Stadtteil von Mainz"),
    ("Mainz-Weisenau", 4, "Stadtteil von Mainz"),
    ("Mainz-Laubenheim", 7, "Stadtteil von Mainz"),
    ("Mainz-Ebersheim", 9, "Stadtteil von Mainz"),
    ("Mainz-Hechtsheim", 6, "Stadtteil von Mainz"),
    # Rheinhessen
    ("Nierstein", 15, "Rheinhessen"),
    ("Schwabsburg", 17, "Ortsteil von Nierstein, Rheinhessen"),
    ("Oppenheim", 20, "Rheinhessen"),
    ("Dienheim", 19, "Ortsteil von Oppenheim"),
    ("Guntersblum", 24, "Rheinhessen"),
    ("Ludwigshöhe", 22, "Rheinhessen"),
    ("Alsheim", 28, "Rheinhessen"),
    ("Osthofen", 33, "Rheinhessen"),
    ("Worms", 42, "Rheinhessen / Rhein"),
    ("Bodenheim", 10, "Rheinhessen"),
    ("Nackenheim", 13, "Rheinhessen"),
    ("Harxheim", 8, "Rheinhessen"),
    ("Lörzweiler", 12, "Rheinhessen"),
    ("Selzen", 15, "Rheinhessen"),
    ("Hahnheim", 16, "Rheinhessen"),
    ("Undenheim", 17, "Rheinhessen"),
    ("Köngernheim", 18, "Rheinhessen"),
    ("Friesenheim (Rheinhessen)", 30, "Rheinhessen"),
    ("Mommenheim", 18, "Rheinhessen"),
    ("Zornheim", 10, "Rheinhessen"),
    ("Sörgenloch", 14, "Rheinhessen"),
    ("Klein-Winternheim", 8, "Rheinhessen"),
    ("Ober-Olm", 11, "Rheinhessen"),
    ("Essenheim", 13, "Rheinhessen"),
    ("Stadecken-Elsheim", 15, "Rheinhessen"),
    ("Wörrstadt", 22, "Rheinhessen"),
    ("Sprendlingen", 26, "Rheinhessen"),
    ("Gau-Bischofsheim", 9, "Rheinhessen"),
    ("Nieder-Olm", 10, "Rheinhessen"),
    ("Alzey", 30, "Rheinhessen"),
    ("Framersheim", 26, "Rheinhessen"),
    ("Flonheim", 28, "Rheinhessen"),
    ("Gau-Odernheim", 24, "Rheinhessen"),
    ("Wöllstein", 30, "Rheinhessen"),
    ("Bad Kreuznach", 40, "Nahe"),
    ("Bingen am Rhein", 30, "Rhein"),
    ("Ingelheim am Rhein", 15, "Rhein"),
    ("Gau-Algesheim", 20, "Rheinhessen"),
    ("Heidesheim am Rhein", 12, "Rheinhessen"),
    ("Budenheim", 8, "Rheinhessen"),
    # Wiesbaden & Umgebung
    ("Wiesbaden", 10, "Hessische Landeshauptstadt"),
    ("Wiesbaden-Biebrich", 8, "Stadtteil von Wiesbaden"),
    ("Wiesbaden-Schierstein", 9, "Stadtteil von Wiesbaden"),
    ("Mainz-Kastel", 4, "Stadtteil von Wiesbaden, rechtsrheinisch"),
    ("Mainz-Kostheim", 6, "Stadtteil von Wiesbaden, rechtsrheinisch"),
    ("Wiesbaden-Erbenheim", 14, "Stadtteil von Wiesbaden"),
    ("Wiesbaden-Bierstadt", 13, "Stadtteil von Wiesbaden"),
    ("Wiesbaden-Dotzheim", 12, "Stadtteil von Wiesbaden"),
    ("Taunusstein", 20, "Taunus"),
    ("Idstein", 30, "Taunus"),
    ("Hofheim am Taunus", 25, "Taunus"),
    # Rheingau
    ("Eltville am Rhein", 20, "Rheingau"),
    ("Walluf", 17, "Rheingau"),
    ("Oestrich-Winkel", 25, "Rheingau"),
    ("Geisenheim", 30, "Rheingau"),
    ("Rüdesheim am Rhein", 35, "Rheingau"),
    ("Lorch", 42, "Rheingau"),
    ("Kiedrich", 22, "Rheingau"),
    # Rhein-Main / Taunus (östlich)
    ("Rüsselsheim am Main", 20, "Rhein-Main"),
    ("Kelsterbach", 24, "Rhein-Main"),
    ("Raunheim", 24, "Rhein-Main"),
    ("Groß-Gerau", 25, "Rhein-Main"),
    ("Mörfelden-Walldorf", 28, "Rhein-Main"),
    ("Frankfurt am Main", 35, "Rhein-Main"),
    ("Offenbach am Main", 40, "Rhein-Main"),
    ("Neu-Isenburg", 38, "Rhein-Main"),
    ("Langen", 32, "Rhein-Main"),
    ("Egelsbach", 30, "Rhein-Main"),
    ("Dreieich", 35, "Rhein-Main"),
    ("Eschborn", 32, "Taunus"),
    ("Schwalbach am Taunus", 30, "Taunus"),
    ("Kronberg im Taunus", 35, "Taunus"),
    ("Königstein im Taunus", 38, "Taunus"),
    ("Oberursel (Taunus)", 36, "Taunus"),
    ("Bad Homburg vor der Höhe", 45, "Taunus"),
    ("Darmstadt", 35, "Rhein-Main"),
    ("Ginsheim-Gustavsburg", 15, "Rhein-Main"),
    # außerhalb des Einsatzgebiets (Beispiele)
    ("Aschaffenburg", 68, "außerhalb des Einsatzgebiets"),
    ("Koblenz", 62, "außerhalb des Einsatzgebiets"),
    ("Mannheim", 58, "außerhalb des Einsatzgebiets"),
    ("Heidelberg", 62, "außerhalb des Einsatzgebiets"),
    ("Kaiserslautern", 63, "außerhalb des Einsatzgebiets"),
    ("Gießen", 68, "außerhalb des Einsatzgebiets"),
    ("Fulda", 110, "außerhalb des Einsatzgebiets"),
    ("Karlsruhe", 100, "außerhalb des Einsatzgebiets"),
    ("Trier", 115, "außerhalb des Einsatzgebiets"),
]

def location_search_widget():
    import json
    data = json.dumps(
        [{"name": n, "distance": d, "note": note, "core": n in ALWAYS_SERVED}
         for n, d, note in SEARCH_LOCATIONS],
        ensure_ascii=False,
    )
    return f'''<div class="location-search" data-radius="{RADIUS_KM}">
  <div class="location-search-heading">
    <span class="eyebrow">Einsatzgebiet prüfen</span>
    <h3>Sind wir auch in Ihrem Ort tätig? Jetzt in Sekunden nachsehen.</h3>
  </div>
  <div class="location-search-box">
    <input type="text" id="ort-suche" class="location-search-input" placeholder="Ort eingeben, z. B. Schwabsburg, Nierstein, Frankfurt …" autocomplete="off" aria-label="Ort eingeben und Einsatzgebiet prüfen">
    <button type="button" class="location-search-btn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS["search"]}</svg><span class="btn-label">Suche starten</span></button>
    <div class="location-search-suggestions"></div>
  </div>
  <div class="location-search-result"></div>
  <script type="application/json" class="location-search-data">{data}</script>
</div>'''

# CDN für Leaflet (echtes, minimalistisches Kartenmaterial: CartoDB "Positron":
# helle, reduzierte Kacheln ohne Werbe-/Kontrastfarben, kostenlos & ohne API-Key).
LEAFLET_CDN = '''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>'''

# Echte Koordinaten (WGS84) der auf der Übersichtskarte markierten Orte.
# Bewusst auf wenige Orte reduziert, um einen schnellen visuellen Eindruck vom
# Einsatzgebiet zu vermitteln (Nähe/Distanz in alle Richtungen).
MAP_POINTS = [
    dict(name="Mainz", lat=49.9929, lon=8.2473, dist=None, main=True),
    dict(name="Wiesbaden", lat=50.0782, lon=8.2398, dist=10),
    dict(name="Frankfurt am Main", lat=50.1109, lon=8.6821, dist=35),
    dict(name="Bingen am Rhein", lat=49.9686, lon=7.8994, dist=30),
    dict(name="Groß-Gerau", lat=49.9169, lon=8.4826, dist=25),
    dict(name="Darmstadt", lat=49.8728, lon=8.6512, dist=35),
]

def location_map_html(container_id="einsatzgebiet-karte"):
    """Echte, minimalistisch gestylte Karte (Leaflet + CartoDB Positron-Kacheln):
    Mainz im Zentrum, 35-km-Radiuskreis, Marker mit Hover-Tooltip für die
    wichtigsten Orte. Zeigt den tatsächlichen Rheinverlauf über echtes Kartenmaterial."""
    import json
    points_json = json.dumps(MAP_POINTS, ensure_ascii=False)
    return f'''<div id="{container_id}" class="leaflet-map" data-points='{points_json}' data-radius-km="{RADIUS_KM}" role="img" aria-label="Karte des Einsatzgebiets: Mainz und {RADIUS_KM} km Radius"></div>'''

# --------------------------------------------------------------------------
# Head / Header / Mega menu / Mobile nav / Footer / Cookie banner
# --------------------------------------------------------------------------

DOMAIN = "https://www.heinand.de"

def canonical_path(relpath):
    """Erzeugt aus einem Datei-Relativpfad die öffentliche URL-Pfadangabe (für canonical/sitemap)."""
    if relpath == "index.html":
        return "/"
    if relpath.endswith("/index.html"):
        return "/" + relpath[: -len("index.html")]
    return "/" + relpath

def head(title, description, prefix, relpath="index.html", noindex=False, extra_css=""):
    url = DOMAIN + canonical_path(relpath)
    robots = "noindex, nofollow" if noindex else "index, follow"
    og_image = f"{DOMAIN}/assets/logo-blue-gold.png"
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="HEINAND Immobilien">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="{prefix}assets/mark-blue.png">
<link rel="stylesheet" href="{prefix}css/style.css">
{local_business_jsonld(prefix)}
{extra_css}
</head>
'''

def local_business_jsonld(prefix):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "HEINAND Immobilien",
  "image": "{DOMAIN}/assets/logo-blue-gold.png",
  "url": "{DOMAIN}/",
  "telephone": "{PHONE_TEL.replace('tel:', '')}",
  "email": "{EMAIL}",
  "priceRange": "$$",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Menimaneweg 4",
    "postalCode": "55130",
    "addressLocality": "Mainz",
    "addressCountry": "DE"
  }},
  "geo": {{
    "@type": "GeoCoordinates",
    "latitude": 49.9929,
    "longitude": 8.2473
  }},
  "areaServed": [
    {",".join(f'{{"@type":"City","name":"{l["name"]}"}}' for l in LOCATIONS)}
  ],
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00",
    "closes": "17:00"
  }}
}}
</script>'''

def faq_jsonld(qa_pairs):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in qa_pairs
        ],
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, ensure_ascii=False, indent=2)}\n</script>'

def header(prefix, active=""):
    def navlink(label, href, key):
        cls = " active" if key == active else ""
        return f'<a href="{prefix}{href}" class="{cls.strip()}">{label}</a>'

    mega_items_verwaltung = "\n".join(
        f'''<li><a href="{prefix}{href}"><strong>{name}</strong><span>{desc}</span></a></li>'''
        for name, href, desc in SERVICES_VERWALTUNG
    )
    mega_items_verkauf = "\n".join(
        f'''<li><a href="{prefix}{href}"><strong>{name}</strong><span>{desc}</span></a></li>'''
        for name, href, desc in SERVICES_VERKAUF
    )

    mobile_links = "\n".join(
        f'<a href="{prefix}{href}">{name}</a>' for name, href, _ in (SERVICES_VERWALTUNG + SERVICES_VERKAUF)
    )

    return f'''<div class="topbar">
  <div class="container">
    <span>Immobilienverwaltung &amp; Verkauf · Mainz, Wiesbaden &amp; Rhein-Main</span>
    <div class="topbar-right">
      <a href="mailto:{EMAIL}">{topbar_icon("mail")} {EMAIL}</a>
      <a href="{PHONE_TEL}">{topbar_icon("phone")} {PHONE}</a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="container">
    {logo_block(prefix, "light", loading="eager")}
    <nav class="main-nav" aria-label="Hauptnavigation">
      <div class="nav-item-dropdown">
        <button type="button" class="nav-dropdown-trigger">Leistungen <span aria-hidden="true">&#9662;</span></button>
        <div class="mega-menu">
          <div>
            <h4>Verwaltung</h4>
            <p class="sub">Laufende Betreuung Ihrer Immobilie</p>
            <ul>{mega_items_verwaltung}</ul>
          </div>
          <div>
            <h4>Verkauf &amp; Bewertung</h4>
            <p class="sub">Wenn sich Ihre Pläne ändern</p>
            <ul>{mega_items_verkauf}</ul>
          </div>
        </div>
      </div>
      {navlink("Region", "region.html", "region")}
      {navlink("Über uns", "ueber-uns.html", "ueber-uns")}
      {navlink("Ratgeber", "blog/index.html", "blog")}
      {navlink("Kontakt", "kontakt.html", "kontakt")}
    </nav>
    <div class="header-actions">
      <a href="{prefix}schadensmeldung.html" class="btn btn-outline-navy">Schaden melden</a>
      <span class="btn btn-outline-navy btn-soon btn-icon-only" aria-disabled="true" title="Kundenportal folgt in Kürze"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS["user"]}</svg><span class="badge-soon">bald</span></span>
      <a href="{prefix}kontakt.html" class="btn btn-navy">Kostenloses Erstgespräch <span aria-hidden="true">&#8594;</span></a>
      <button type="button" class="menu-toggle" aria-label="Menü öffnen">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-nav">
  <div class="mobile-nav-header">
    {logo_block(prefix, "light")}
    <button type="button" class="mobile-nav-close" aria-label="Menü schließen" style="background:none;border:none;font-size:26px;color:#0a2148;">&times;</button>
  </div>
  <a href="{prefix}index.html">Start</a>
  {mobile_links}
  {navlink("Region", "region.html", "")}
  {navlink("Über uns", "ueber-uns.html", "")}
  {navlink("Ratgeber", "blog/index.html", "")}
  {navlink("Kontakt", "kontakt.html", "")}
  <a href="{prefix}schadensmeldung.html">Schaden melden</a>
  <span class="mobile-nav-soon">Kundenportal <span class="badge-soon">bald verfügbar</span></span>
  <a href="{prefix}kontakt.html" class="btn btn-primary">Kostenloses Erstgespräch &#8594;</a>
</div>
'''

def footer(prefix):
    leistungen_links = "\n".join(f'<li><a href="{prefix}{href}">{name}</a></li>' for name, href in FOOTER_LEISTUNGEN)
    unternehmen_links = "\n".join(f'<li><a href="{prefix}{href}">{name}</a></li>' for name, href in FOOTER_UNTERNEHMEN)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <div class="footer-logo">
          <img src="{prefix}assets/logo-white-gold.png" alt="HEINAND Immobilien" class="logo-img" loading="lazy">
        </div>
        <p>Immobilienverwaltung und Verkauf in Mainz und dem Rhein-Main-Gebiet. Digital, strukturiert und transparent: Anliegen werden schnell geklärt, jeder Vorgang ist dokumentiert.</p>
      </div>
      <div class="footer-col">
        <h5>Leistungen</h5>
        <ul>{leistungen_links}</ul>
      </div>
      <div class="footer-col">
        <h5>Unternehmen</h5>
        <ul>{unternehmen_links}</ul>
      </div>
      <div class="footer-col footer-contact">
        <h5>Kontakt</h5>
        <ul>
          <li>Menimaneweg 4<br>55130 Mainz</li>
          <li><a href="{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 HEINAND Immobilien · Mainz</span>
      <div class="footer-bottom-links">
        <a href="{prefix}impressum.html">Impressum</a>
        <a href="{prefix}datenschutz.html">Datenschutz</a>
        <button type="button" data-open-cookie-settings>Cookie-Einstellungen</button>
      </div>
    </div>
  </div>
</footer>
<div class="cookie-banner">
  <h4>Cookie-Einstellungen</h4>
  <p>Wir verwenden ausschließlich technisch notwendige Cookies bzw. vergleichbare Speichertechnologien für den Betrieb dieser Website (z. B. zur Speicherung Ihrer Cookie-Entscheidung). Es findet kein Werbe- oder Drittanbieter-Tracking statt. Details in der <a href="{prefix}datenschutz.html">Datenschutzerklärung</a>.</p>
  <div class="cookie-actions">
    <button type="button" class="btn btn-primary" data-cookie-action="accepted">Alle akzeptieren</button>
    <button type="button" class="btn btn-outline-navy" data-cookie-action="essential">Nur notwendige</button>
  </div>
</div>
<script src="{prefix}js/main.js"></script>
</body>
</html>
'''

def cta_banner(prefix, heading="Weniger Verwaltungsstress. Mehr Kontrolle über Ihre Immobilie.",
               text="Im kostenlosen Erstgespräch analysieren wir Ihr Objekt und zeigen Ihnen, wie eine strukturierte Verwaltung aussieht: unverbindlich und ohne Kleingedrucktes."):
    return f'''<section class="cta-banner">
  <div class="container">
    <div class="mark">{mark_img(prefix, "gold", 64)}</div>
    <h2>{heading}</h2>
    <p style="color:rgba(255,255,255,0.78);max-width:560px;margin:0 auto 30px;">{text}</p>
    <div class="cta-row">
      <a href="{prefix}kontakt.html" class="btn btn-primary">Kostenloses Erstgespräch anfragen <span aria-hidden="true">&#8594;</span></a>
      <a href="{prefix}kontakt.html#termin" class="btn btn-outline">Direkt Termin buchen</a>
    </div>
  </div>
</section>'''

def painpoints_section(eyebrow, headline, points, closing_pre, closing_highlight):
    """Painpoint-Sektion (angelehnt an das vom Kunden gezeigte Referenzdesign
    'Kennen Sie das?'), im HEINAND-Markendesign (Navy/Gold statt Orange).
    points: Liste aus (icon_name, zitat, beschreibung)-Tupeln."""
    cards = "".join(
        f'<div class="painpoint-card">{icon(ic)}<h3>{quote}</h3><p>{desc}</p></div>'
        for ic, quote, desc in points
    )
    return f'''<section class="section-mist painpoints">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{headline}</h2>
    </div>
    <div class="painpoints-grid">{cards}</div>
    <p class="painpoints-closing">{closing_pre} <span class="highlight">{closing_highlight}</span></p>
  </div>
</section>'''

# Motion-Video im Hero-Bereich der Startseite (hinter dem Text ganz oben).
# Quelle: eigenes Drohnenvideo des Kunden (Rundflug um den Mainzer Dom,
# Abendstimmung, leicht verlangsamt): liegt lokal unter assets/video/.
HOME_VIDEO_SRC = "assets/video/mainzer-dom-drohnenflug.mp4"
HOME_VIDEO_POSTER = "assets/video/mainzer-dom-poster.jpg"

def hero_video_html(prefix):
    """Video- und Overlay-Layer für den Hero-Bereich der Startseite. Wird direkt
    hinter <div class="container hero-inner"> in den .hero--video Abschnitt
    eingefügt; der Text liegt dank z-index darüber."""
    return f'''<video class="hero-video" autoplay muted loop playsinline poster="{prefix}{HOME_VIDEO_POSTER}" aria-hidden="true">
    <source src="{prefix}{HOME_VIDEO_SRC}" type="video/mp4">
  </video>
  <div class="hero-video-overlay"></div>'''

def icon_wrap(svg_inner):
    return f'<div class="card-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{svg_inner}</svg></div>'

ICONS = {
    "mail": '<path d="M4 5h16v14H4z"/><path d="M4 6l8 7 8-7"/>',
    "cash": '<circle cx="12" cy="12" r="9"/><path d="M9 9h4a2 2 0 1 1 0 4H9m0-4v8m0-4h4"/>',
    "invoice": '<path d="M6 3h9l3 3v15H6z"/><path d="M9 9h6M9 13h6M9 17h4"/>',
    "wrench": '<circle cx="12" cy="12" r="3.2"/><path d="M12 3.5v3M12 17.5v3M20.5 12h-3M6.5 12h-3M18 6l-2.1 2.1M8.1 15.9L6 18M18 18l-2.1-2.1M8.1 8.1L6 6"/>',
    "home": '<path d="M4 11l8-7 8 7"/><path d="M6 10v10h12V10"/>',
    "chart": '<path d="M4 20V10M12 20V4M20 20v-7"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14.2c2.4.5 4.5 2.6 4.5 5.8"/>',
    "check": '<path d="M20 7L10 17l-5-5"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
    "handshake": '<rect x="2.5" y="9.5" width="7.5" height="5" rx="2.5"/><rect x="14" y="9.5" width="7.5" height="5" rx="2.5"/><path d="M10 12h4"/>',
    "gauge": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M9.2 15.3l2.2-2.6 1.8 1.7 2.6-3.4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
    "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="0.5"/>',
    "bolt": '<path d="M13 3L4 14h6l-1 7 9-11h-6z"/>',
    "trend": '<path d="M4 16l6-6 4 4 6-8"/><path d="M14 6h6v6"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2C10 21 3 14 3 6a2 2 0 0 1 2-2z"/>',
    "pin": '<path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    # Leistungs-spezifische Icons: bewusst gegenständlich statt abstrakt, damit
    # das jeweilige Leistungsfeld auf einen Blick erkennbar ist.
    "key": '<circle cx="7" cy="7" r="3"/><path d="M9.2 9.2L18 18"/><path d="M13.5 13.5l2.2-2.2M16.3 16.3l2.2-2.2"/>',
    "apartments": '<rect x="6" y="3" width="12" height="18" rx="1"/><path d="M6 21h12"/><rect x="8.7" y="6" width="2" height="2"/><rect x="13.3" y="6" width="2" height="2"/><rect x="8.7" y="10" width="2" height="2"/><rect x="13.3" y="10" width="2" height="2"/><rect x="8.7" y="14" width="2" height="2"/><rect x="13.3" y="14" width="2" height="2"/>',
    "apartment-unit": '<rect x="6" y="3" width="12" height="18" rx="1"/><path d="M6 21h12"/><rect x="8.7" y="6" width="2" height="2"/><rect x="13.3" y="6" width="2" height="2"/><rect x="8.7" y="14" width="2" height="2"/><rect x="13.3" y="14" width="2" height="2"/><rect x="13.3" y="10" width="2" height="2"/><rect x="8.7" y="10" width="2" height="2" fill="currentColor" stroke="none"/>',
    "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M12 3.5v3M12 17.5v3M20.5 12h-3M6.5 12h-3M18 6l-2.1 2.1M8.1 15.9L6 18M18 18l-2.1-2.1M8.1 8.1L6 6"/>',
    "tag": '<path d="M11 3h6a2 2 0 0 1 2 2v6l-9 9-8-8z"/><circle cx="15.5" cy="7.5" r="1.3" fill="currentColor" stroke="none"/>',
    "doc-trend": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M9.2 15.3l2.2-2.6 1.8 1.7 2.6-3.4"/>',
    "user": '<circle cx="12" cy="8" r="3.4"/><path d="M5 20c0-3.9 3.1-7 7-7s7 3.1 7 7"/>',
}

def icon(name):
    return icon_wrap(ICONS.get(name, ICONS["check"]))

def feature_icon(name):
    return f'<div class="feature-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(name, ICONS["check"])}</svg></div>'

def contact_icon(name):
    return f'<div class="ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(name, ICONS["check"])}</svg></div>'

def topbar_icon(name):
    """Kleines SVG-Icon für die Topbar (Mail/Telefon): bewusst als Vektor statt
    Unicode-Symbol, damit beide Icons garantiert exakt gleich groß sind."""
    return f'<svg class="topbar-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS.get(name, ICONS["check"])}</svg>'


