#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from components import (
    ROOT, head, header, footer, cta_banner, hero_video_html, icon, feature_icon, contact_icon,
    mark_svg, mark_img, PHONE, PHONE_TEL, EMAIL, SERVICES_VERWALTUNG, SERVICES_VERKAUF,
    LOCATIONS, location_map_html, LEAFLET_CDN, DOMAIN, canonical_path, faq_jsonld, location_search_widget,
    painpoints_section,
)

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", relpath)

def page(title, description, prefix, active, body, relpath="index.html", noindex=False, extra_css=""):
    return head(title, description, prefix, relpath, noindex, extra_css) + "<body>\n" + header(prefix, active) + body + footer(prefix)

ALL_SERVICES = SERVICES_VERWALTUNG + SERVICES_VERKAUF  # (name, href, desc)

SERVICE_ICONS = {
    "leistungen/mietverwaltung.html": "key",
    "leistungen/weg-verwaltung.html": "apartments",
    "leistungen/se-verwaltung.html": "apartment-unit",
    "leistungen/werterhalt-instandhaltung.html": "gear",
    "leistungen/immobilienverkauf.html": "tag",
    "leistungen/immobilienbewertung.html": "doc-trend",
}

TIER1_LOCATIONS = [l for l in LOCATIONS if l.get("tier") == 1]
TIER2_LOCATIONS = [l for l in LOCATIONS if l.get("tier") != 1]

def locations_section(prefix, heading="Verwaltung, Werterhalt und Verkauf in Mainz und im gesamten 35-km-Umkreis.",
                       intro="Wir sind dort für Sie da, wo wir uns auskennen: mit Miet-, WEG- und Sondereigentumsverwaltung, Werterhalt sowie Immobilienverkauf und -bewertung in Mainz und einem Radius von rund 35 Kilometern — von Wiesbaden über Rheinhessen bis ins Rhein-Main-Gebiet. Kurze Wege bedeuten schnelle Objektbegehungen, kurzfristige Übergaben und ein Handwerkernetzwerk, das wirklich vor Ort ist.",
                       show_cta=True, standorte_prefix=None, map_id="einsatzgebiet-karte"):
    """Standorte-Sektion mit echter Leaflet-Radius-Karte + vollständiger Ortsliste.
    standorte_prefix: Pfad-Präfix zu /standorte/ (Default: prefix + 'standorte/')."""
    sp = standorte_prefix if standorte_prefix is not None else f"{prefix}standorte/"
    tier1_links = "".join(
        f'<a href="{sp}{l["slug"]}.html"><span class="dot"></span>Hausverwaltung {l["name"]}</a>'
        for l in TIER1_LOCATIONS
    )
    tier2_text = ", ".join(l["name"] for l in TIER2_LOCATIONS)
    cta_html = f'<a href="{prefix}region.html" class="btn btn-outline-navy" style="margin-top:8px;">Alle Standorte im Überblick</a>' if show_cta else ""
    return f'''<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Unsere Region</span>
      <h2>{heading}</h2>
      <p style="margin-top:16px;color:#5b6472;">{intro}</p>
    </div>
    <div class="locations-grid">
      <div class="map-card">{location_map_html(map_id)}</div>
      <div>
        <p class="eyebrow" style="display:block;margin-bottom:10px;">Standorte mit eigener Betreuung vor Ort</p>
        <div class="locations-tier1">{tier1_links}</div>
        <p class="locations-tier2-list"><strong>Weitere Orte im Einzugsgebiet:</strong> {tier2_text} und Umgebung.</p>
        {cta_html}
      </div>
    </div>
  </div>
</section>'''

# ==========================================================================
# HOME
# ==========================================================================

def build_home():
    prefix = ""
    home_faq = [
        ("Was kostet eine Hausverwaltung bei HEINAND?", "Das hängt von Objektgröße, Einheitenzahl und Leistungsumfang ab. Im kostenlosen Erstgespräch analysieren wir Ihr Objekt und machen Ihnen ein transparentes Festangebot — ohne versteckte Zusatzkosten."),
        ("Wie läuft der Wechsel von unserer bisherigen Verwaltung ab?", "Strukturiert: Wir kümmern uns um die Übernahme aller Unterlagen, Konten und laufenden Vorgänge von Ihrer Vorverwaltung. Für Eigentümer und Mieter läuft der Wechsel ohne Bruch — Sie merken nur, dass es besser funktioniert."),
        ("In welchen Regionen sind Sie tätig?", "Unser Schwerpunkt liegt in Mainz und einem Radius von rund 35 km — darunter Wiesbaden, Ingelheim, Bingen, Alzey, Rüsselsheim und Nieder-Olm. Auch Bad Kreuznach zählt als feste Standort-Region zu unserem Einzugsgebiet. Kurze Wege sind Teil unseres Qualitätsversprechens."),
        ("Wie schnell reagieren Sie bei Schäden?", "Jede Schadensmeldung wird priorisiert: Akute Gefahren behandeln wir sofort, dringende Reparaturen zeitnah, reguläre Anliegen strukturiert und nachvollziehbar. Über unser Online-Formular ist Ihr Anliegen in zwei Minuten gemeldet."),
        ("Verwalten Sie auch einzelne Eigentumswohnungen?", "Ja — mit der Sondereigentumsverwaltung betreuen wir Ihre vermietete Wohnung komplett, inklusive Mieterkontakt und Schnittstelle zur WEG-Verwaltung. Ideal für Kapitalanleger, die nicht vor Ort sind."),
    ]
    body = f'''
<section class="hero hero--video">
  {hero_video_html(prefix)}
  <div class="container hero-inner">
    <span class="eyebrow">Mainz · Wiesbaden · Rhein-Main</span>
    <h1>Immobilienverwaltung, die digital arbeitet — schnell, transparent, immer aktuell.</h1>
    <p class="hero-lead">Miet-, WEG- und Sondereigentumsverwaltung sowie Immobilienverkauf in Mainz und dem Rhein-Main-Gebiet. Als digital arbeitende Verwaltung sind wir bei jedem Objekt auf dem aktuellen Stand und klären Anliegen, bevor sie zu Problemen werden — damit Eigentum kein zweiter Job ist.</p>
    <div class="hero-cta">
      <a href="{prefix}kontakt.html" class="btn btn-primary">Kostenloses Erstgespräch <span aria-hidden="true">&#8594;</span></a>
      <a href="{prefix}leistungen/index.html" class="btn btn-outline">Leistungen entdecken</a>
    </div>
    <div class="hero-stats">
      <span>100&nbsp;% digitale Vorgangsverwaltung</span>
      <span>7 Jahre Verwaltungserfahrung</span>
      <span>Anliegen schnell geklärt</span>
    </div>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Unsere Leistungen</span>
      <h2>Verwaltung, Werterhalt und Verkauf — alles aus einer Hand.</h2>
    </div>
    <div class="cards-grid">
      {"".join(service_card(prefix, n, h, d, ic) for n, h, d, ic in [
          ("Mietverwaltung", SERVICES_VERWALTUNG[0][1], SERVICES_VERWALTUNG[0][2], "key"),
          ("WEG-Verwaltung", SERVICES_VERWALTUNG[1][1], SERVICES_VERWALTUNG[1][2], "apartments"),
          ("Sondereigentumsverwaltung", SERVICES_VERWALTUNG[2][1], SERVICES_VERWALTUNG[2][2], "apartment-unit"),
          ("Werterhalt & Instandhaltung", SERVICES_VERWALTUNG[3][1], SERVICES_VERWALTUNG[3][2], "gear"),
          ("Immobilienbewertung", SERVICES_VERKAUF[1][1], SERVICES_VERKAUF[1][2], "doc-trend"),
          ("Immobilienverkauf", SERVICES_VERKAUF[0][1], SERVICES_VERKAUF[0][2], "tag"),
      ])}
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Warum HEINAND</span>
      <h2>Vertrauen entsteht durch klare Prozesse.</h2>
      <p style="margin-top:16px;color:#5b6472;">Viele Eigentümer kennen Verwaltung als Blackbox: Niemand erreichbar, nichts dokumentiert, alles dauert. Wir arbeiten anders — mit regionalem Verständnis, digitaler Struktur und Kommunikation, auf die Sie sich verlassen können.</p>
      <a href="{prefix}ueber-uns.html" class="btn btn-outline-navy" style="margin-top:20px;">Lernen Sie uns kennen</a>
    </div>
    <div class="feature-grid">
      {feature("bolt", "Effizienz", "Wir nehmen Ihnen den Koordinationsaufwand ab: Mieter, Handwerker, Abrechnungen — alles läuft über uns.")}
      {feature("trend", "Werterhalt", "Regelmäßige Objektbetreuung und schnelle Reaktion verhindern, dass kleine Schäden groß werden.")}
      {feature("chart", "Transparenz", "Digitale Vorgangsverwaltung und nachvollziehbares Reporting: Sie sehen jederzeit, was passiert.")}
      {feature("shield", "Verlässlichkeit", "Digitale Prozesse statt Zettelwirtschaft: Jedes Anliegen wird erfasst, priorisiert und verbindlich geklärt — nichts bleibt liegen.")}
    </div>
  </div>
</section>

<section class="section-mist">
  <div class="container two-col">
    <div>
      <span class="eyebrow">Digital &amp; erreichbar</span>
      <h2 style="margin-top:10px;">Schaden melden in zwei Minuten — mit klarer Priorisierung.</h2>
      <p style="margin-top:16px;color:#5b6472;">Mieter und Eigentümer melden Anliegen über unser strukturiertes Online-Formular. Jede Meldung wird eingestuft — regulär, dringend oder akut — und entsprechend schnell bearbeitet. Nichts geht verloren, alles ist dokumentiert.</p>
      <ul class="process-list">
        <li>{icon("bolt")}<span><b>Akute Gefahren:</b> sofortige Reaktion</span></li>
        <li>{icon("chart")}<span><b>Digitale Vorgangsverwaltung</b> mit Statusverfolgung</span></li>
        <li>{icon("gear")}<span><b>Regionales Handwerkernetzwerk</b> mit kurzen Wegen</span></li>
      </ul>
      <a href="{prefix}schadensmeldung.html" class="btn btn-primary" style="margin-top:28px;">Zum Schadensformular <span aria-hidden="true">&#8594;</span></a>
    </div>
    <div>
      <div class="card" style="margin-bottom:16px;"><strong style="color:var(--navy-deep);">Sofort-Einsatz koordiniert</strong><br><span style="font-size:13px;color:#b3441f;">Dringend · Heizungsausfall</span></div>
      <div class="card" style="margin-bottom:16px;"><strong style="color:var(--navy-deep);">Handwerker beauftragt</strong><br><span style="font-size:13px;color:var(--gold);">Regulär · Klemmendes Fenster</span></div>
      <div class="card"><strong style="color:var(--navy-deep);">Termin in Planung</strong></div>
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">So starten wir</span>
      <h2>In fünf Schritten zu einer Verwaltung, die funktioniert.</h2>
    </div>
    <div class="steps-grid steps-grid-5">
      {step("01", "Objektbegehung", "Wir schauen uns Ihr Objekt und Ihre Situation vor Ort an — unverbindlich, ohne Verkaufsdruck, und mit Blick für das, was wirklich zählt.")}
      {step("02", "Unverbindliches Angebot", "Auf Basis der Begehung erhalten Sie ein transparentes, auf Ihr Objekt zugeschnittenes Angebot — klar kalkuliert, ohne versteckte Kosten.")}
      {step("03", "Beschlussfassung", "Bei WEGs begleiten wir die Beschlussfassung zur Verwalterbestellung; bei Miet- und Sondereigentum reicht Ihre Zusage zur Beauftragung.")}
      {step("04", "Kommunikation mit dem Vorverwalter", "Wir übernehmen die Abstimmung mit Ihrer bisherigen Verwaltung und die vollständige Dokumentenübergabe — Sie müssen sich um nichts kümmern.")}
      {step("05", "Laufende Betreuung", "Ab Tag eins laufen alle Vorgänge digital: Anliegen werden online gemeldet und schnell geklärt — und Sie haben wieder Zeit für das Wesentliche.")}
    </div>
    <p style="text-align:center;margin-top:28px;">
      <a href="{prefix}leistungen/verwalterwechsel.html" style="color:var(--navy);text-decoration:underline;font-weight:600;">Verwalterwechsel bei einer WEG im Detail: der komplette Ablauf Schritt für Schritt &rarr;</a>
    </p>
  </div>
</section>

<section class="section-cream" style="padding-bottom:0;">
  <div class="container">
    {location_search_widget()}
  </div>
</section>

{locations_section(prefix)}

<section class="section-white">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Häufige Fragen</span>
      <h2>Was Eigentümer uns am häufigsten fragen.</h2>
    </div>
    <div class="faq">
      {"".join(faq_item(q, a) for q, a in home_faq)}
    </div>
  </div>
</section>

{cta_banner(prefix)}
'''
    write("index.html", page(
        "Hausverwaltung Mainz & Rhein-Main | HEINAND Immobilien",
        "Hausverwaltung in Mainz, Wiesbaden & 35 km Umkreis: Miet-, WEG- & SE-Verwaltung, Verkauf. 100 % digital, 7 Jahre Erfahrung. Jetzt kostenlos anfragen.",
        prefix, "home", body, relpath="index.html", extra_css=faq_jsonld(home_faq) + LEAFLET_CDN
    ))

def service_card(prefix, name, href, desc, ic):
    return f'''<div class="card">
  {icon(ic)}
  <h3>{name}</h3>
  <p>{desc}</p>
  <a href="{prefix}{href}" class="card-link">Mehr erfahren <span aria-hidden="true">&#8594;</span></a>
</div>'''

def feature(ic, name, desc):
    return f'''<div class="feature-item">{feature_icon(ic)}<h4>{name}</h4><p>{desc}</p></div>'''

def step(num, title, desc):
    return f'''<div class="step"><div class="step-num">{num}</div><h3>{title}</h3><p>{desc}</p></div>'''

def faq_item(q, a):
    return f'''<div class="faq-item">
  <button type="button" class="faq-q"><span>{q}</span><span class="icon" aria-hidden="true">+</span></button>
  <div class="faq-a"><p>{a}</p></div>
</div>'''

# ==========================================================================
# LEISTUNGEN — Übersicht
# ==========================================================================

def build_leistungen_index():
    prefix = "../"
    verwaltung_icons = ["key", "apartments", "apartment-unit", "gear"]
    verkauf_icons = ["tag", "doc-trend"]
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Leistungen</span>
    <h1>Alles, was Ihre Immobilie braucht — aus einer Hand.</h1>
    <p class="hero-lead">Von der laufenden Verwaltung über den Werterhalt bis zum Verkauf: Wir betreuen Eigentümer, Kapitalanleger und Eigentümergemeinschaften in Mainz und dem Rhein-Main-Gebiet.</p>
  </div>
</section>
<section class="section-cream">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Verwaltung</span>
      <h2>Laufende Betreuung Ihrer Immobilie</h2>
    </div>
    <div class="cards-grid">
      {"".join(service_card(prefix, n, h, d, ic) for (n, h, d), ic in zip(SERVICES_VERWALTUNG, verwaltung_icons))}
    </div>
  </div>
</section>
<section class="section-white">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Verkauf &amp; Bewertung</span>
      <h2>Wenn sich Ihre Pläne ändern</h2>
    </div>
    <div class="cards-grid">
      {"".join(service_card(prefix, n, h, d, ic) for (n, h, d), ic in zip(SERVICES_VERKAUF, verkauf_icons))}
    </div>
  </div>
</section>
{cta_banner(prefix)}
'''
    write("leistungen/index.html", page(
        "Leistungen — Hausverwaltung & Verkauf in Mainz | HEINAND",
        "Alle Leistungen von HEINAND Immobilien in Mainz & Rhein-Main: Miet-, WEG- & SE-Verwaltung, Werterhalt, Bewertung und Verkauf.",
        prefix, "leistungen", body, relpath="leistungen/index.html"
    ))

# ==========================================================================
# LEISTUNGEN — Detailseiten (generisches Template)
# ==========================================================================

def select_field(label, options, required=True):
    opts = "".join(f'<option>{o}</option>' for o in options)
    star = " *" if required else ""
    return f'''<div class="form-field">
  <label>{label}{star}</label>
  <select><option value="">Bitte wählen…</option>{opts}</select>
</div>'''

def text_field(label, placeholder="", required=True, full=False):
    star = " *" if required else ""
    cls = " full" if full else ""
    return f'''<div class="form-field{cls}">
  <label>{label}{star}</label>
  <input type="text" placeholder="{placeholder}">
</div>'''

def service_detail_page(slug, name, eyebrow_extra, h1, lead, features, advantages, form_heading, form_intro, form_fields_html, submit_label, form_title="Angebot anfragen", pain_points=None, detail_link=None):
    prefix = "../"
    others = [s for s in ALL_SERVICES if s[1] != f"leistungen/{slug}.html"][:3]
    adv_html = "".join(f'<li>{icon("check")}<span>{a}</span></li>' for a in advantages)
    others_html = "".join(service_card(prefix, n, h, d, SERVICE_ICONS.get(h, "check")) for n, h, d in others)
    detail_link_html = ""
    if detail_link:
        dl_href, dl_label = detail_link
        detail_link_html = f'<a href="{dl_href}" class="btn btn-outline-navy" style="margin-top:18px;">{dl_label}</a>'
    pain_html = ""
    if pain_points:
        pain_html = painpoints_section(
            "Kennen Sie das?",
            "Sätze, die jeder Eigentümer ständig hört und satt hat.",
            pain_points,
            "Das liegt selten am einzelnen Objekt. Es liegt an einer Verwaltung, die reagiert, statt zu führen.",
            "Genau da setzen wir an.",
        )

    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">{name}&nbsp;· Mainz &amp; Rhein-Main</span>
    <h1>{h1}</h1>
    <p class="hero-lead">{lead}</p>
    <div class="hero-cta">
      <a href="#anfrage" class="btn btn-primary">Jetzt kostenlos anfragen</a>
      <a href="{PHONE_TEL}" class="btn btn-outline">{PHONE}</a>
    </div>
  </div>
</section>

{pain_html}

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <h2>Das übernehmen wir für Sie.</h2>
    </div>
    <div class="cards-grid">
      {"".join(f'<div class="card">{icon(ic)}<h3>{t}</h3><p>{d}</p></div>' for t, d, ic in features)}
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container two-col">
    <div>
      <span class="eyebrow">Ihr Vorteil</span>
      <h2 style="margin-top:10px;">{form_heading}</h2>
      <ul class="process-list" style="margin-top:24px;">
        {adv_html}
      </ul>
      {detail_link_html}
    </div>
    <div id="anfrage" class="form-card">
      <span class="eyebrow">In 2 Minuten angefragt</span>
      <h3 style="margin-top:10px;margin-bottom:6px;">{form_title}</h3>
      <p style="color:#5b6472;font-size:14px;margin-bottom:6px;">{form_intro}</p>
      <form data-contact-form data-form-name="{name} — Angebotsanfrage">
        <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
        <div class="form-step-label">1. Eckdaten zu Ihrem Anliegen</div>
        <div class="form-grid">
          {form_fields_html}
        </div>
        <div class="form-step-label">2. Wie erreichen wir Sie?</div>
        <div class="form-grid">
          {text_field("Ihr Name", "", True)}
          {text_field("E-Mail", "", True)}
          {text_field("Telefon (optional)", "", False)}
          {text_field("Anmerkung (optional)", "", False)}
        </div>
        <button type="submit" class="btn btn-primary form-submit">{submit_label}</button>
        <p class="form-note">Kostenlos und unverbindlich. Mit dem Absenden erklären Sie sich mit der Verarbeitung Ihrer Daten zur Bearbeitung der Anfrage einverstanden (<a href="{prefix}datenschutz.html">Datenschutz</a>).</p>
      </form>
    </div>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head">
      <h2 style="font-size:26px;">Weitere Leistungen</h2>
    </div>
    <div class="cards-grid">{others_html}</div>
  </div>
</section>

{cta_banner(prefix)}
'''
    write(f"leistungen/{slug}.html", page(
        f"{name} Mainz — {eyebrow_extra} | HEINAND",
        lead[:155],
        prefix, "leistungen", body, relpath=f"leistungen/{slug}.html"
    ))

def build_services():
    service_detail_page(
        "mietverwaltung", "Mietverwaltung", "für Mietobjekte",
        "Ihre Mietobjekte in guten Händen — ohne dass Sie sich um alles kümmern müssen.",
        "Mieterkorrespondenz, Zahlungseingänge, Nebenkostenabrechnung, Handwerkerkoordination: Ein vermietetes Objekt bedeutet laufende Arbeit. Wir übernehmen die komplette kaufmännische und technische Betreuung Ihrer Mietimmobilie — digital, strukturiert und dokumentiert, damit jedes Anliegen schnell geklärt ist.",
        [
            ("Mieterkorrespondenz", "Wir sind erste Anlaufstelle für Ihre Mieter — verbindlich, schnell und dokumentiert.", "mail"),
            ("Mietinkasso & Mahnwesen", "Überwachung der Zahlungseingänge, konsequentes Mahnwesen, Anpassung der Mieten im rechtlichen Rahmen.", "cash"),
            ("Nebenkostenabrechnung", "Fristgerechte, nachvollziehbare Betriebskostenabrechnung — die häufigste Fehlerquelle in Eigenregie.", "invoice"),
            ("Reparaturkoordination", "Schäden werden priorisiert (regulär, dringend, akut) und über unser regionales Handwerkernetzwerk gelöst.", "wrench"),
            ("Neuvermietung", "Von der Vermarktung über Besichtigungen und Bonitätsprüfung bis zur Übergabe.", "search"),
            ("Reporting", "Sie sehen jederzeit, was mit Ihrer Immobilie passiert — transparent und strukturiert.", "chart"),
        ],
        ["Anliegen werden digital erfasst, priorisiert und schnell geklärt", "Regionales Handwerkernetzwerk mit fairen Konditionen", "Fristgerechte Abrechnungen ohne Formfehler", "Volle Transparenz durch digitale Vorgangsverwaltung"],
        "Lassen Sie uns über Ihr Mietobjekt sprechen — kostenlos und unverbindlich.",
        "Ein paar Angaben zu Ihrem Objekt genügen — wir machen Ihnen ein transparentes Festangebot für die komplette Betreuung.",
        select_field("Objektart", ["Einzelne Wohnung(en)", "Mehrfamilienhaus", "Mehrere Objekte / Portfolio", "Gewerbeeinheit(en)"]) +
        select_field("Anzahl Mieteinheiten", ["1–2", "3–10", "11–30", "Über 30"]) +
        text_field("Objekt-Standort", "", True) +
        select_field("Aktuell verwaltet durch", ["Eigenregie", "Andere Verwaltung (Wechsel)", "Neukauf / noch offen"]),
        "Angebot anfragen",
        form_title="Angebot für Ihre Mietverwaltung anfragen",
        pain_points=[
            ("mail", "„Der Mieter meldet sich – und keiner ruft zurück.“", "Anliegen bleiben liegen, weil niemand klar zuständig ist."),
            ("invoice", "„Die Nebenkostenabrechnung dauert Monate.“", "Oder sie stimmt am Ende einfach nicht — Streit ist vorprogrammiert."),
            ("cash", "„Ich weiß nie, ob die Miete pünktlich kommt.“", "Ohne System verliert man schnell den Überblick über Zahlungseingänge."),
            ("wrench", "„Ein Rohrbruch – und keiner weiß, wer kommt.“", "Ohne Handwerkernetzwerk wird jeder Schaden zur Odyssee."),
        ]
    )

    service_detail_page(
        "weg-verwaltung", "WEG-Verwaltung", "für Ihre WEG",
        "WEG-Verwaltung, die Beschlüsse umsetzt — nicht nur verwaltet.",
        "Viele Eigentümergemeinschaften kennen das: Versammlungen ohne Ergebnis, Beschlüsse, die liegen bleiben, Abrechnungen, die niemand nachvollziehen kann. Wir führen Ihre WEG mit klaren Prozessen, sauberer Buchhaltung und verbindlicher Kommunikation — damit Verwaltung wieder Vertrauenssache ist.",
        [
            ("Eigentümerversammlungen", "Ordnungsgemäße Einberufung, Durchführung und Protokollierung — auch hybrid.", "users"),
            ("Wirtschaftsplan & Jahresabrechnung", "Nachvollziehbare Hausgeldabrechnung und vorausschauende Wirtschaftsplanung.", "invoice"),
            ("Beschlussumsetzung", "Beschlüsse werden dokumentiert, terminiert und konsequent umgesetzt.", "check"),
            ("Instandhaltungsmanagement", "Regelmäßige Objektbegehungen, Wartungsverträge, Erhaltungsrücklage im Blick.", "wrench"),
            ("Rechtssicherheit", "Verwaltung nach aktuellem WEG-Recht, sauber dokumentiert.", "shield"),
            ("Kommunikation", "Verbindliche, schnelle Kommunikation mit Beirat und Eigentümern — digital dokumentiert, jederzeit nachvollziehbar.", "mail"),
        ],
        ["Verbindliche Umsetzung statt Verwaltung auf Sicht", "Transparente Abrechnungen, die Eigentümer verstehen", "Strukturierte Übernahme von der Vorverwaltung", "Regionale Präsenz: kurze Wege zu Ihren Objekten"],
        "Unzufrieden mit Ihrer aktuellen Verwaltung? Wir übernehmen strukturiert.",
        "Nennen Sie uns die Eckdaten Ihrer Gemeinschaft — Sie erhalten ein transparentes Angebot mit Leistungskatalog, ohne Kleingedrucktes.",
        select_field("Anzahl Einheiten", ["Bis 10", "11–20", "21–50", "Über 50"]) +
        text_field("Objekt-Standort", "", True) +
        select_field("Ihre Rolle", ["Beiratsvorsitz", "Verwaltungsbeirat", "Eigentümer:in", "Bauträger"]) +
        select_field("Aktuelle Situation", ["Verwalterwechsel geplant", "Unzufrieden, erst informieren", "Aktuell ohne Verwaltung", "Neubau / Erstbestellung"]),
        "WEG-Angebot anfragen",
        form_title="Angebot für Ihre WEG anfragen",
        pain_points=[
            ("check", "„Die Beschlüsse von der letzten Versammlung? Liegen noch.“", "Ohne konsequente Umsetzung bleibt jede Versammlung wirkungslos."),
            ("phone", "„Der Verwalter ist gerade nicht erreichbar.“", "Für Beirat und Eigentümer heißt das: warten, ohne Antwort."),
            ("invoice", "„Die Jahresabrechnung verstehe ich nicht.“", "Unklare Hausgeldabrechnungen sorgen jedes Jahr für Ärger."),
            ("mail", "„Anfragen an den Beirat verschwinden im Nichts.“", "Ohne dokumentierte Prozesse geht viel einfach unter."),
        ],
        detail_link=("verwalterwechsel.html", "So läuft ein Verwalterwechsel ab — Schritt für Schritt")
    )

    service_detail_page(
        "se-verwaltung", "Sondereigentumsverwaltung", "für Anleger",
        "Ihre Eigentumswohnung rentiert — wir kümmern uns um den Rest.",
        "Die WEG-Verwaltung kümmert sich ums Gemeinschaftseigentum — aber wer betreut Ihre vermietete Wohnung? Als Sondereigentumsverwaltung übernehmen wir alles, was Ihre Wohnung betrifft: vom Mieterkontakt über die Abrechnung bis zur Abstimmung mit der Hausverwaltung. Ideal für Kapitalanleger, die nicht vor Ort sind.",
        [
            ("Mieterbetreuung", "Kommunikation, Anliegen und Übergaben — wir sind vor Ort, Sie müssen es nicht sein.", "users"),
            ("Miet- und Nebenkostenabrechnung", "Korrekte Abrechnung inklusive Umlage der Hausgeldpositionen.", "invoice"),
            ("Schnittstelle zur WEG", "Wir vertreten Ihre Interessen gegenüber der Gemeinschafts-Verwaltung.", "handshake"),
            ("Instandhaltung im Sondereigentum", "Koordination von Reparaturen in der Wohnung über unser Netzwerk.", "wrench"),
            ("Neuvermietung", "Marktgerechte Wiedervermietung bei Mieterwechsel — inklusive Bonitätsprüfung.", "search"),
            ("Eigentümerversammlung", "Auf Wunsch nehmen wir mit Vollmacht an Versammlungen teil.", "doc"),
        ],
        ["Perfekt für Anleger, die nicht in Mainz wohnen", "Alles digital geregelt — von der Meldung bis zur Abrechnung", "Ihre Interessen werden in der WEG aktiv vertreten", "Digitale Dokumentation aller Vorgänge"],
        "Kapitalanlage ohne Aufwand — sprechen Sie mit uns.",
        "Ideal für Kapitalanleger: Sagen Sie uns kurz, um welche Wohnung(en) es geht — wir übernehmen den Rest.",
        select_field("Anzahl Wohnungen", ["1", "2–5", "Mehr als 5"]) +
        text_field("Objekt-Standort", "", True) +
        select_field("Vermietungsstand", ["Vermietet", "Aktuell leer / Neuvermietung nötig", "Teilweise vermietet"]) +
        select_field("Ihr Wohnort", ["In der Region Rhein-Main", "Außerhalb der Region", "Im Ausland"]),
        "SE-Verwaltung anfragen",
        form_title="SE-Verwaltung anfragen",
        pain_points=[
            ("pin", "„Ich wohne weit weg und weiß nicht, was in meiner Wohnung passiert.“", "Ohne jemanden vor Ort bleibt vieles im Dunkeln."),
            ("apartment-unit", "„Die WEG-Verwaltung kümmert sich nicht um mein Sondereigentum.“", "Für Ihre eigene Wohnung ist meist niemand konkret zuständig."),
            ("users", "„Mieterwechsel? Ich erfahre es zu spät.“", "Ohne feste Ansprechperson vor Ort verpasst man wichtige Momente."),
            ("doc", "„Keiner vertritt meine Interessen in der Eigentümerversammlung.“", "Als Kapitalanleger sitzen Sie sonst nicht mit am Tisch."),
        ]
    )

    service_detail_page(
        "immobilienverkauf", "Immobilienverkauf", "Makler mit Know-how",
        "Verkaufen Sie nicht irgendwie — verkaufen Sie richtig.",
        "Ein Immobilienverkauf ist für die meisten Eigentümer eine Entscheidung, die sie nur wenige Male im Leben treffen. Wir begleiten Sie vom ersten Gespräch über die realistische Preisfindung bis zum Notartermin — mit der Marktkenntnis von 7 Jahren Verwaltung im Rhein-Main-Gebiet.",
        [
            ("Werteinschätzung", "Realistische Preisfindung auf Basis regionaler Marktdaten — keine Lockangebote.", "gauge"),
            ("Exposé & Vermarktung", "Professionelle Aufbereitung, Fotos und Platzierung auf den relevanten Kanälen.", "doc"),
            ("Besichtigungsmanagement", "Vorqualifizierte Interessenten, koordinierte Termine, keine Besichtigungstouristen.", "search"),
            ("Bonitätsprüfung", "Wir prüfen Finanzierungsbestätigungen, bevor es ernst wird.", "shield"),
            ("Verhandlung", "Wir verhandeln in Ihrem Interesse — sachlich und mit klarem Ziel.", "handshake"),
            ("Begleitung bis zum Notar", "Kaufvertragsabstimmung, Notartermin, Übergabeprotokoll — alles aus einer Hand.", "check"),
        ],
        ["Verwalter-Perspektive: Wir kennen Objekte von innen", "Regionales Netzwerk aus Käufern und Kapitalanlegern", "Diskreter Verkauf ohne öffentliche Vermarktung möglich", "Klare Kommunikation über jeden Schritt"],
        "Was ist Ihre Immobilie wert? Fragen Sie uns — kostenlos.",
        "Ein paar Eckdaten genügen — wir melden uns innerhalb eines Werktags mit einer ersten Einschätzung und besprechen das weitere Vorgehen.",
        select_field("Objektart", ["Eigentumswohnung", "Einfamilienhaus", "Mehrfamilienhaus", "Grundstück", "Gewerbe"]) +
        text_field("Ort / Stadtteil", "", True) +
        text_field("Wohnfläche (ca. m²)", "", False) +
        text_field("Baujahr (ca.)", "", False) +
        select_field("Aktueller Zustand", ["Frei / selbst genutzt", "Vermietet", "Teilweise vermietet"]) +
        select_field("Zeithorizont", ["So bald wie möglich", "In 3–6 Monaten", "Ich orientiere mich erst"]),
        "Verkaufsberatung anfragen",
        form_title="Kostenlose Verkaufsberatung anfragen"
    )

    service_detail_page(
        "immobilienbewertung", "Immobilienbewertung", "Werteinschätzung",
        "Zahlen statt Bauchgefühl — was Ihre Immobilie wirklich wert ist.",
        "Ob Verkauf, Neuvermietung, Erbschaft oder einfach ein aktueller Überblick: Eine fundierte Bewertung ist die Grundlage jeder guten Entscheidung. Wir bewerten Ihre Immobilie auf Basis regionaler Marktdaten, Objektzustand und Lagequalität — ehrlich, auch wenn die Zahl mal nicht schmeichelt.",
        [
            ("Marktwertermittlung", "Vergleichswert-, Ertragswert- oder Sachwertverfahren — je nach Objekttyp.", "gauge"),
            ("Mietwertanalyse", "Welche Miete ist marktgerecht und rechtlich durchsetzbar?", "chart"),
            ("Lage- und Objektanalyse", "Mikrolage, Zustand, Entwicklungspotenzial — dokumentiert und nachvollziehbar.", "pin"),
            ("Verkaufs- oder Halten-Empfehlung", "Wir sagen Ihnen auch, wenn Halten die bessere Option ist.", "target"),
        ],
        ["Echte regionale Marktdaten statt Online-Rechner", "Ehrliche Einschätzung ohne Verkaufsdruck", "Grundlage für Verkauf, Finanzierung oder Nachlass", "Kostenlos im Rahmen eines Erstgesprächs"],
        "Kostenlose Werteinschätzung anfragen — in 48 Stunden beim Erstgespräch.",
        "Sagen Sie uns, worum es geht — Sie erhalten eine fundierte Einschätzung auf Basis echter regionaler Marktdaten, keine Online-Rechner-Zahl.",
        select_field("Objektart", ["Eigentumswohnung", "Einfamilienhaus", "Mehrfamilienhaus", "Grundstück", "Gewerbe"]) +
        text_field("Ort / Stadtteil", "", True) +
        text_field("Wohnfläche (ca. m²)", "", False) +
        text_field("Baujahr (ca.)", "", False) +
        select_field("Anlass der Bewertung", ["Verkauf geplant", "Erbschaft / Nachlass", "Kaufpreis prüfen", "Vermögensübersicht", "Sonstiges"]),
        "Werteinschätzung anfragen",
        form_title="Kostenlose Werteinschätzung anfragen"
    )

    service_detail_page(
        "werterhalt-instandhaltung", "Werterhalt & Instandhaltung", "Objektpflege",
        "Kleine Schäden bleiben klein — wenn jemand hinschaut.",
        "Der Wert einer Immobilie entsteht nicht beim Kauf, sondern im Betrieb. Aufgeschobene Wartung und verschleppte Reparaturen kosten am Ende ein Vielfaches. Wir sorgen mit regelmäßigen Begehungen, klarer Priorisierung und einem eingespielten Handwerkernetzwerk dafür, dass Ihr Objekt in Schuss bleibt.",
        [
            ("Objektbegehungen", "Regelmäßige Kontrolle von Gebäude, Technik und Außenanlagen.", "search"),
            ("Priorisierte Schadensabwicklung", "Regulär, dringend oder akut — jede Meldung wird eingestuft und entsprechend schnell gelöst.", "bolt"),
            ("Wartungsmanagement", "Heizung, Aufzug, Brandschutz: Wartungsverträge und Prüffristen im Blick.", "clock"),
            ("Handwerkerkoordination", "Regionale Betriebe, geprüfte Qualität, faire Preise.", "wrench"),
            ("Instandhaltungsplanung", "Vorausschauende Maßnahmenplanung statt teurer Überraschungen.", "chart"),
            ("Digitale Dokumentation", "Jeder Vorgang nachvollziehbar — vom Eingang bis zur Abnahme.", "doc"),
        ],
        ["Akute Gefahren werden sofort behandelt", "Werterhalt durch Prävention statt Reparaturstau", "Regionale Handwerker mit kurzen Wegen", "Volle Kostentransparenz je Maßnahme"],
        "Schluss mit Reparaturstau — wir strukturieren die Instandhaltung.",
        "Beschreiben Sie kurz Ihr Objekt — wir schauen es uns an und zeigen Ihnen, wo Handlungsbedarf besteht und was warten kann.",
        select_field("Objektart", ["Eigentumswohnung", "Einfamilienhaus", "Mehrfamilienhaus", "Gewerbe"]) +
        text_field("Objekt-Standort", "", True) +
        select_field("Worum geht es?", ["Reparaturstau aufarbeiten", "Laufende Wartung organisieren", "Objektbegehung gewünscht", "Konkreter Schaden"]),
        "Check anfragen",
        form_title="Instandhaltungs-Check anfragen",
        pain_points=[
            ("bolt", "„Der kleine Schaden wurde erst teuer, als niemand hinschaute.“", "Ohne regelmäßige Kontrolle wird aus wenig schnell viel."),
            ("clock", "„Wartungstermine? Nie im Blick.“", "Verpasste Prüffristen bei Heizung oder Aufzug werden schnell zum Risiko."),
            ("wrench", "„Der Handwerker kommt, wenn er Zeit hat.“", "Ohne festes Netzwerk warten Sie, statt dass gehandelt wird."),
            ("doc", "„Niemand dokumentiert, was wann gemacht wurde.“", "Ohne Nachweise fehlt am Ende jede Übersicht über den Zustand."),
        ]
    )

def wechsel_step(num, badges, title, desc, dauer=None):
    badge_html = "".join(f'<span class="badge {b[0]}">{b[1]}</span>' for b in badges)
    dauer_html = f'<span class="wechsel-dauer">{dauer}</span>' if dauer else ""
    return f'''<div class="wechsel-step">
      <div class="wechsel-step-num">{num}</div>
      <div>
        <div class="wechsel-badges">{badge_html}{dauer_html}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>
    </div>'''

def build_verwalterwechsel():
    prefix = "../"
    B_HEINAND = ("badge-heinand", "HEINAND")
    B_VORVERWALTUNG = ("badge-vorverwaltung", "Vorverwaltung")
    B_EIGENTUEMER = ("badge-eigentuemer", "Eigentümer / Beirat")

    steps_html = "".join([
        wechsel_step("1", [B_EIGENTUEMER, B_HEINAND],
            "Kontaktaufnahme & Erstgespräch",
            "Sie oder Ihr Verwaltungsbeirat nehmen Kontakt zu uns auf — telefonisch, per Formular oder direkt vor Ort. Im unverbindlichen Erstgespräch klären wir Ihre aktuelle Situation, die Größe der Gemeinschaft und den Grund für den geplanten Wechsel.",
            "ca. 30–45 Min."),
        wechsel_step("2", [B_HEINAND],
            "Objektbegehung & Bestandsaufnahme",
            "Wir besichtigen das Gemeinschaftseigentum, sichten vorhandene Unterlagen (soweit verfügbar) und verschaffen uns ein Bild vom Zustand des Objekts, offenen Instandhaltungsthemen und der wirtschaftlichen Lage der Gemeinschaft.",
            "ca. 1 Woche"),
        wechsel_step("3", [B_HEINAND],
            "Erstellung eines unverbindlichen Angebots",
            "Auf Basis der Begehung erstellen wir ein transparentes Angebot mit Leistungskatalog und Vergütung — ohne versteckte Kosten. Sie oder der Beirat erhalten es zur Prüfung und können es mit weiteren Angeboten vergleichen.",
            "ca. 3–5 Werktage"),
        wechsel_step("4", [B_EIGENTUEMER, B_HEINAND],
            "Antrag zur Aufnahme des Tagesordnungspunkts",
            "Damit über den Wechsel überhaupt abgestimmt werden kann, muss der Punkt „Abberufung der Verwaltung und Neubestellung“ auf die Tagesordnung der nächsten Eigentümerversammlung. Eigentümer, die mindestens ein Viertel der Stimmen vertreten, können dies gemäß § 24 Abs. 2 WEG von der aktuellen Verwaltung verlangen. Wir unterstützen Sie bei der Formulierung des Antrags (Musterschreiben weiter unten).",
            "ca. 1 Woche Vorlauf"),
        wechsel_step("5", [B_VORVERWALTUNG],
            "Einberufung der Eigentümerversammlung",
            "Solange sie noch amtiert, ist die aktuelle Verwaltung verpflichtet, form- und fristgerecht (in der Regel mit mindestens drei Wochen Vorlauf) zur Versammlung einzuladen und den beantragten Tagesordnungspunkt aufzunehmen.",
            "gesetzl. Frist"),
        wechsel_step("6", [B_EIGENTUEMER],
            "Beschlussfassung in der Eigentümerversammlung",
            "Die Gemeinschaft stimmt über die Abberufung der bisherigen und die Neubestellung der neuen Verwaltung ab. Seit der WEG-Reform reicht dafür die einfache Mehrheit der abgegebenen Stimmen — eine Begründung ist nicht mehr erforderlich. Eine Musterformulierung für den Beschluss finden Sie weiter unten.",
            "1 Versammlung, ca. 1–2 Std."),
        wechsel_step("7", [B_HEINAND],
            "Kommunikation mit der Vorverwaltung",
            "Nach dem Beschluss übernehmen wir die gesamte Abstimmung mit der bisherigen Verwaltung — von der Bestätigung des Beschlusses bis zur Klärung des Übergabetermins. Sie müssen selbst nicht mehr mit der Vorverwaltung sprechen.",
            "ca. 1–2 Wochen"),
        wechsel_step("8", [B_VORVERWALTUNG, B_HEINAND],
            "Dokumenten- und Kontenübergabe",
            "Die Vorverwaltung ist gesetzlich verpflichtet, sämtliche Unterlagen herauszugeben: Beschlusssammlung, Protokolle, Verträge, Versicherungsunterlagen, technische Dokumentation sowie das Verwaltungsvermögen inklusive Erhaltungsrücklage. Wir prüfen die Vollständigkeit anhand einer Übergabe-Checkliste und fordern fehlende Unterlagen aktiv nach.",
            "ca. 2–4 Wochen"),
        wechsel_step("9", [B_HEINAND],
            "Ummeldung von Konten, Verträgen & Versicherungen",
            "Wir melden die Gemeinschaft bei Banken, Versicherern und Dienstleistern um, richten die laufenden Konten auf unseren Namen als Verwaltung um und übernehmen bestehende Wartungs- und Dienstleistungsverträge oder kündigen sie bei Bedarf neu.",
            "ca. 1–2 Wochen"),
        wechsel_step("10", [B_HEINAND],
            "Laufende Betreuung startet",
            "Ab dem vereinbarten Übernahmestichtag laufen alle Vorgänge über HEINAND: Mieteranliegen, Instandhaltung, Buchhaltung und Kommunikation mit dem Beirat — strukturiert, digital dokumentiert und jederzeit nachvollziehbar.",
            "ab Stichtag"),
    ])

    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">WEG-Verwaltung &middot; Verwalterwechsel</span>
    <h1>Der Verwalterwechsel — Schritt für Schritt erklärt.</h1>
    <p class="hero-lead">Ein Wechsel der WEG-Verwaltung klingt aufwendig, ist es für Sie als Eigentümer aber kaum: Der überwiegende Teil der Arbeit liegt bei uns und bei der bisherigen Verwaltung. Hier sehen Sie den kompletten Ablauf — von der ersten Kontaktaufnahme bis zur laufenden Betreuung.</p>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Wer macht was?</span>
      <h2>Ihr Aufwand als Eigentümer bleibt minimal.</h2>
      <p style="max-width:640px;margin:14px auto 0;color:#5b6472;">Die eigentliche Arbeit — Angebot, Übergabe, Ummeldungen — übernehmen wir und, im Rahmen ihrer gesetzlichen Pflichten, die bisherige Verwaltung. Von Ihnen braucht es im Regelfall nur einen Antrag und Ihre Stimme in der Versammlung.</p>
    </div>
    <div class="task-split">
      <div class="col heinand">
        <h3>HEINAND</h3>
        <ul>
          <li>Erstgespräch, Begehung und Angebot</li>
          <li>Unterstützung beim TOP-Antrag und der Beschlussformulierung</li>
          <li>Komplette Kommunikation mit der Vorverwaltung</li>
          <li>Prüfung der Übergabe-Checkliste, Nachforderung fehlender Unterlagen</li>
          <li>Ummeldung von Konten, Versicherungen und Dienstleisterverträgen</li>
          <li>Start der laufenden Betreuung</li>
        </ul>
      </div>
      <div class="col vorverwaltung">
        <h3>Vorverwaltung</h3>
        <ul>
          <li>Fristgerechte Einberufung der Versammlung</li>
          <li>Aufnahme des beantragten Tagesordnungspunkts</li>
          <li>Protokollierung des Beschlusses</li>
          <li>Vollständige Herausgabe aller Unterlagen und Konten</li>
          <li>Übertrag der Erhaltungsrücklage</li>
        </ul>
      </div>
      <div class="col eigentuemer">
        <h3>Eigentümer / Beirat</h3>
        <ul>
          <li>Antrag auf Aufnahme des Tagesordnungspunkts stellen</li>
          <li>Teilnahme an der Eigentümerversammlung</li>
          <li>Abstimmung über den Beschluss</li>
          <li>Das war's — den Rest übernehmen wir</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container" style="max-width:900px;">
    <div class="section-head center">
      <span class="eyebrow">Der Ablauf im Detail</span>
      <h2>10 Schritte von der Kontaktaufnahme bis zur laufenden Betreuung.</h2>
    </div>
    <div class="wechsel-steps">
      {steps_html}
    </div>
  </div>
</section>

<section class="section-cream">
  <div class="container" style="max-width:820px;">
    <div class="section-head center">
      <span class="eyebrow">Musterformulierungen</span>
      <h2>Vorschläge für Antrag und Beschluss.</h2>
      <p style="margin-top:14px;color:#5b6472;">Die folgenden Formulierungen dienen als Orientierung und können an Ihre konkrete Gemeinschaftsordnung und Situation angepasst werden.</p>
    </div>

    <div class="sample-doc" style="margin-top:32px;">
      <span class="doc-label">Muster · Antrag zur Aufnahme eines Tagesordnungspunkts</span>
      <p>An die Verwaltung<br>[Name der bisherigen Hausverwaltung]<br>[Anschrift]</p>
      <p>[Ort, Datum]</p>
      <p><strong>Antrag auf Ergänzung der Tagesordnung der nächsten Eigentümerversammlung gemäß § 24 Abs. 2 WEG</strong></p>
      <p>Sehr geehrte Damen und Herren,</p>
      <p>hiermit beantrage(n) der/die unterzeichnende(n) Wohnungseigentümer, die gemäß beigefügter Unterschriftenliste mindestens ein Viertel der Miteigentumsanteile der Wohnungseigentümergemeinschaft [Bezeichnung der WEG, Anschrift] vertreten, die Aufnahme des folgenden Tagesordnungspunkts in die nächste ordentliche Eigentümerversammlung:</p>
      <p>„Abberufung der bestellten Verwaltung [Name Vorverwaltung] und Neubestellung der HEINAND Immobilien, Inhaber Philipp Hartung, als neue Verwaltung der Gemeinschaft ab dem [gewünschtes Datum], sowie Beschlussfassung über den Abschluss des entsprechenden Verwaltervertrags.“</p>
      <p>Wir bitten um form- und fristgerechte Einladung gemäß § 24 Abs. 4 WEG unter Berücksichtigung des beantragten Tagesordnungspunkts sowie um Übersendung der Einladung an alle Wohnungseigentümer.</p>
      <p>Mit freundlichen Grüßen<br>[Name(n), Unterschrift(en) der antragstellenden Eigentümer]</p>
    </div>

    <div class="sample-doc" style="margin-top:24px;">
      <span class="doc-label">Muster · Beschlussformulierung in der Versammlung</span>
      <p><strong>TOP [Nummer]: Abberufung der Verwaltung und Neubestellung</strong></p>
      <p>„Die Wohnungseigentümergemeinschaft [Bezeichnung, Anschrift] beschließt:</p>
      <p>1. Die [Name Vorverwaltung] wird mit Wirkung zum [Datum] als Verwaltung der Gemeinschaft abberufen. Der bestehende Verwaltervertrag wird zu diesem Zeitpunkt ordentlich gekündigt bzw. einvernehmlich aufgehoben.</p>
      <p>2. Die HEINAND Immobilien, Inhaber Philipp Hartung, Menimaneweg 4, 55130 Mainz, wird mit Wirkung zum [Datum] zur neuen Verwaltung der Gemeinschaft im Sinne des § 26 WEG bestellt. Die Bestellung erfolgt für die Dauer von [z. B. drei Jahren / bis zum TT.MM.JJJJ] gemäß § 26 Abs. 2 WEG.</p>
      <p>3. Der Verwaltungsbeirat bzw. die/der Vorsitzende wird ermächtigt, den Verwaltervertrag mit der HEINAND Immobilien zu den im Angebot vom [Datum] genannten Konditionen im Namen der Gemeinschaft zu unterzeichnen.“</p>
      <p><em>Abstimmungsergebnis: Ja-Stimmen [ ] · Nein-Stimmen [ ] · Enthaltungen [ ] — Beschluss angenommen mit einfacher Mehrheit gemäß § 25 Abs. 1 WEG.</em></p>
    </div>

    <div class="disclaimer-box">
      <strong>Wichtiger Hinweis:</strong> Die vorstehenden Formulierungen sind unverbindliche Muster zur Orientierung und stellen keine Rechtsberatung dar. Ob und in welcher Form ein Antrag oder Beschluss in Ihrer konkreten Gemeinschaft rechtssicher ist, hängt von der individuellen Gemeinschaftsordnung, der Beschlusssammlung und dem Einzelfall ab. Wir empfehlen, Anträge und Beschlussvorlagen vor der Versammlung von einem Fachanwalt für WEG-Recht oder einer vergleichbar qualifizierten Stelle prüfen zu lassen. HEINAND Immobilien ist keine Rechtsanwaltskanzlei und übernimmt keine Haftung für die rechtliche Wirksamkeit der Muster.
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container" style="max-width:640px;text-align:center;">
    <span class="eyebrow">Nächster Schritt</span>
    <h2 style="margin-top:10px;">Sprechen wir über Ihre Gemeinschaft.</h2>
    <p style="color:#5b6472;margin-top:12px;">Ob Sie schon einen Beschluss geplant haben oder ganz am Anfang stehen — wir begleiten Sie durch den kompletten Wechsel.</p>
    <div class="hero-cta" style="justify-content:center;margin-top:20px;">
      <a href="weg-verwaltung.html#anfrage" class="btn btn-primary">WEG-Angebot anfragen</a>
      <a href="{PHONE_TEL}" class="btn btn-outline-navy">{PHONE}</a>
    </div>
  </div>
</section>

{cta_banner(prefix)}
'''
    write("leistungen/verwalterwechsel.html", page(
        "Verwalterwechsel WEG Schritt für Schritt | HEINAND",
        "So läuft ein Verwalterwechsel bei einer WEG ab: TOP-Antrag, Beschluss, Übergabe. Mit Musterformulierungen und klarer Aufgabenteilung.",
        prefix, "leistungen", body, relpath="leistungen/verwalterwechsel.html"
    ))

build_leistungen_index()
build_services()
build_verwalterwechsel()
print("leistungen done")

# ==========================================================================
# REGION
# ==========================================================================

def build_region():
    prefix = ""
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Unsere Region</span>
    <h1>Mainz, Wiesbaden und Rheinhessen — wir verwalten, wo wir zuhause sind.</h1>
    <p class="hero-lead">Unser Einzugsgebiet umfasst Mainz und einen Radius von rund 35 Kilometern — plus Bad Kreuznach als feste Standort-Region. Diese bewusste Begrenzung ist ein Qualitätsversprechen: kurze Wege, schnelle Vor-Ort-Termine und echte Ortskenntnis.</p>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    {location_search_widget()}
  </div>
</section>

<section class="section-white">
  <div class="container region-grid">
    <div class="card">{icon("pin")}<h3>Mainz</h3><p>Unser Zuhause und Schwerpunkt — von der Altstadt über die Neustadt bis Gonsenheim, Bretzenheim, Laubenheim und Weisenau.</p></div>
    <div class="card">{icon("pin")}<h3>Wiesbaden</h3><p>Direkt über den Rhein: Wir betreuen Objekte in der hessischen Landeshauptstadt mit derselben Präsenz wie in Mainz.</p></div>
    <div class="card">{icon("pin")}<h3>Rheinhessen</h3><p>Ingelheim, Bodenheim, Nieder-Olm und das Umland — gewachsene Wohnlagen mit stabiler Nachfrage.</p></div>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Orte im Überblick</span>
      <h2>Vom Herzen von Mainz bis an den Rand des Rhein-Main-Gebiets.</h2>
    </div>
    <div class="chip-row" style="justify-content:center;">
      {"".join(f'<span class="chip">{c}</span>' for c in ["Mainz-Altstadt","Mainz-Gonsenheim","Wiesbaden","Mainz-Kastel","Ingelheim am Rhein","Bingen am Rhein","Nieder-Olm","Nierstein","Oppenheim","Gau-Algesheim","Bodenheim","Alzey","Wörrstadt","Bad Kreuznach","Rüsselsheim am Main","Groß-Gerau","Frankfurt am Main","Darmstadt","Rüdesheim am Rhein","Eltville am Rhein","Idstein","Taunusstein","Bad Homburg vor der Höhe"])}
    </div>
    <p style="text-align:center;margin-top:24px;color:#5b6472;">Ihr Ort ist hier nicht aufgeführt? Nutzen Sie die Ortssuche oben — oder <a href="{prefix}kontakt.html" style="color:var(--navy);text-decoration:underline;">sprechen Sie uns direkt an</a>.</p>
  </div>
</section>

{locations_section(prefix, heading="Alle Orte im 35-km-Einzugsgebiet auf einen Blick.", intro="Unten sehen Sie unser Einzugsgebiet auf der Karte: Mainz im Zentrum, ca. 35 km Radius, plus Bad Kreuznach als feste Standort-Region. Für die größten Städte im Umkreis bieten wir eine eigene, lokale Betreuung mit entsprechender Marktkenntnis.", show_cta=False, map_id="einsatzgebiet-karte-region")}

<section class="section-white">
  <div class="container">
    <div class="section-head center">
      <h2>Warum ein regionaler Verwalter den Unterschied macht.</h2>
    </div>
    <div class="feature-grid" style="grid-template-columns:repeat(3,1fr);">
      {feature("bolt", "Schnell vor Ort", "Bei akuten Schäden oder Übergaben sind wir in Minuten am Objekt — nicht am Telefon in einer anderen Stadt.")}
      {feature("handshake", "Regionales Netzwerk", "Handwerker, Dienstleister und Behördenkontakte, die wir seit Jahren kennen und deren Qualität wir einschätzen können.")}
      {feature("chart", "Marktkenntnis", "Wir wissen, welche Miete in Gonsenheim realistisch ist und was ein Käufer in Weisenau zahlt — aus eigener Verwaltungspraxis.")}
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a href="{prefix}leistungen/index.html" class="btn btn-outline-navy">Alle Leistungen ansehen</a>
    </div>
  </div>
</section>

{cta_banner(prefix)}
'''
    write("region.html", page(
        "Einzugsgebiet Mainz, Wiesbaden & Rhein-Main | HEINAND",
        "Unser Einzugsgebiet: Mainz und 35 km Umkreis — Wiesbaden, Ingelheim, Bingen, Alzey, Bad Kreuznach u.v.m. Karte & alle Standorte im Überblick.",
        prefix, "region", body, relpath="region.html", extra_css=LEAFLET_CDN
    ))

build_region()
print("region done")

# ==========================================================================
# STANDORTE — lokale Landingpages (SEO: "Hausverwaltung <Ort>")
# ==========================================================================

def build_standort(loc):
    prefix = "../"
    name = loc["name"]
    slug = loc["slug"]
    dist = loc["distance"]
    blurb = loc["blurb"]
    others = [l for l in TIER1_LOCATIONS if l["slug"] != slug][:3]
    others_html = "".join(f'''<a href="{o['slug']}.html" class="card">
  {icon("pin")}
  <h3>Hausverwaltung {o['name']}</h3>
  <p>{o['blurb']}</p>
  <span class="card-link">Mehr erfahren <span aria-hidden="true">&#8594;</span></span>
</a>''' for o in others)
    services_html = "".join(
        f'<div class="card">{icon(SERVICE_ICONS.get(href, "check"))}<h3>{sname}</h3><p>{sdesc}</p><a href="{prefix}{href}" class="card-link">Mehr erfahren <span aria-hidden="true">&#8594;</span></a></div>'
        for sname, href, sdesc in ALL_SERVICES
    )
    standort_faq = [
        (f"Verwaltet HEINAND Immobilien auch in {name}?", f"Ja — {name} liegt ca. {dist} km von unserem Sitz in Mainz entfernt und gehört zu unserem festen Einzugsgebiet. Wir betreuen dort Mietobjekte, Eigentumswohnungen und Eigentümergemeinschaften mit derselben digitalen Struktur wie in Mainz."),
        ("Wie schnell sind Sie bei einem Schaden vor Ort?", f"Akute Schäden behandeln wir sofort, dringende Anliegen in der Regel innerhalb von 24 Stunden. Durch unser regionales Handwerkernetzwerk sind wir auch in {name} schnell handlungsfähig."),
        (f"Was kostet eine Hausverwaltung in {name}?", "Das hängt von Objektgröße und Leistungsumfang ab. Im kostenlosen Erstgespräch analysieren wir Ihr Objekt und machen ein transparentes Festangebot — ohne versteckte Zusatzkosten."),
    ]
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Hausverwaltung {name}&nbsp;· ca. {dist}&nbsp;km von Mainz</span>
    <h1>Hausverwaltung in {name} — digital, transparent, persönlich vor Ort.</h1>
    <p class="hero-lead">{blurb} Als Hausverwaltung aus Mainz betreuen wir Eigentümer, Kapitalanleger und Eigentümergemeinschaften in {name} mit derselben digitalen Struktur und kurzen Reaktionszeiten wie in unserer Heimatstadt.</p>
    <div class="hero-cta">
      <a href="{prefix}kontakt.html" class="btn btn-primary">Kostenloses Erstgespräch <span aria-hidden="true">&#8594;</span></a>
      <a href="{PHONE_TEL}" class="btn btn-outline">{PHONE}</a>
    </div>
    <div class="hero-stats">
      <span>ca. {dist} km von Mainz entfernt</span>
      <span>Regionales Handwerkernetzwerk</span>
      <span>100&nbsp;% digitale Vorgangsverwaltung</span>
    </div>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Leistungen in {name}</span>
      <h2>Verwaltung, Werterhalt und Verkauf — auch in {name}.</h2>
      <p style="margin-top:16px;color:#5b6472;">Alle HEINAND-Leistungen stehen Eigentümern in {name} in vollem Umfang zur Verfügung — von der laufenden Mietverwaltung bis zum Immobilienverkauf.</p>
    </div>
    <div class="cards-grid">{services_html}</div>
  </div>
</section>

<section class="section-white">
  <div class="container two-col">
    <div>
      <span class="eyebrow">Warum HEINAND in {name}</span>
      <h2 style="margin-top:10px;">Regionale Nähe trifft digitale Struktur.</h2>
      <ul class="process-list" style="margin-top:24px;">
        <li>{icon("pin")}<span><b>Kurze Wege:</b> ca. {dist} km von unserem Sitz in Mainz — schnelle Vor-Ort-Termine und Objektbegehungen in {name}.</span></li>
        <li>{icon("bolt")}<span><b>Schnelle Reaktion:</b> Schadensmeldungen aus {name} werden priorisiert und zeitnah über unser Handwerkernetzwerk gelöst.</span></li>
        <li>{icon("chart")}<span><b>Digitale Vorgangsverwaltung:</b> Sie sehen jederzeit, was mit Ihrer Immobilie in {name} passiert.</span></li>
        <li>{icon("handshake")}<span><b>Persönlicher Kontakt:</b> Ein fester Ansprechpartner, kein anonymes Callcenter.</span></li>
      </ul>
    </div>
    <div class="form-card">
      <span class="eyebrow">Kostenlos &amp; unverbindlich</span>
      <h3 style="margin-top:10px;margin-bottom:6px;">Erstgespräch für Ihre Immobilie in {name}</h3>
      <p style="color:#5b6472;font-size:14px;margin-bottom:6px;">Kurze Objektbeschreibung genügt — wir melden uns innerhalb eines Werktags mit einer ersten Einschätzung.</p>
      <form data-contact-form data-form-name="Erstgespräch {name}">
        <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
        <div class="form-grid">
          {select_field("Objektart", ["Einzelne Wohnung(en)", "Mehrfamilienhaus", "WEG / Eigentümergemeinschaft", "Sonstiges"])}
          {text_field("Adresse / Stadtteil in " + name, "", True)}
          {text_field("Ihr Name", "", True)}
          {text_field("E-Mail", "", True)}
        </div>
        <button type="submit" class="btn btn-primary form-submit">Erstgespräch anfragen</button>
        <p class="form-note">Kostenlos und unverbindlich. Mit dem Absenden erklären Sie sich mit der Verarbeitung Ihrer Daten einverstanden (<a href="{prefix}datenschutz.html">Datenschutz</a>).</p>
      </form>
    </div>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Häufige Fragen</span>
      <h2>Hausverwaltung {name} — kurz erklärt.</h2>
    </div>
    <div class="faq">
      {"".join(faq_item(q, a) for q, a in standort_faq)}
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container">
    <div class="section-head">
      <h2 style="font-size:26px;">Weitere Standorte</h2>
    </div>
    <div class="cards-grid">{others_html}</div>
  </div>
</section>

{cta_banner(prefix, f"Eigentum in {name} sollte kein zweiter Job sein.", f"Im kostenlosen Erstgespräch analysieren wir Ihr Objekt in {name} und zeigen Ihnen, wie eine strukturierte Verwaltung aussieht.")}
'''
    write(f"standorte/{slug}.html", page(
        f"Hausverwaltung {name} | HEINAND Immobilien",
        f"Hausverwaltung in {name} (ca. {dist} km von Mainz): Miet- & WEG-Verwaltung, Verkauf. Digital, schnell, persönlich. Jetzt kostenlos anfragen.",
        prefix, "region", body, relpath=f"standorte/{slug}.html", extra_css=faq_jsonld(standort_faq)
    ))

def build_standorte():
    for loc in TIER1_LOCATIONS:
        build_standort(loc)

build_standorte()
print("standorte done")

# ==========================================================================
# ÜBER UNS
# ==========================================================================

def build_ueber_uns():
    prefix = ""
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Über HEINAND Immobilien</span>
    <h1>Eigentum sollte kein zweiter Job sein — dafür arbeiten wir.</h1>
    <p class="hero-lead">Seit 7 Jahren verwalten wir Immobilien in Mainz und dem Rhein-Main-Gebiet. Was uns antreibt: Verwaltung, bei der Eigentümer wissen, was passiert — und sich um nichts kümmern müssen.</p>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="stats-grid" style="margin:0;">
      <div class="stat"><div class="num">7+</div><div class="label">Jahre Verwaltungserfahrung</div></div>
      <div class="stat"><div class="num">35&nbsp;km</div><div class="label">Radius rund um Mainz</div></div>
      <div class="stat"><div class="num">3</div><div class="label">Prioritätsstufen je Schadensfall</div></div>
      <div class="stat"><div class="num">100&nbsp;%</div><div class="label">digitale Vorgangsverwaltung</div></div>
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Unsere Philosophie</span>
      <h2>Immobilienverwaltung mit Verantwortung, Nähe und Weitblick.</h2>
    </div>
    <div class="prose-block">
      <p>Eine Immobilie ist weit mehr als nur ein Gebäude. Sie ist ein Zuhause, eine Altersvorsorge, eine Investition und häufig das Ergebnis jahrelanger Arbeit. Genau deshalb verdient sie eine Verwaltung, die nicht nur Zahlen, Verträge und Fristen im Blick behält, sondern auch die Menschen dahinter versteht.</p>
      <p>Bei HEINAND Immobilien verbinden wir persönliche Betreuung mit modernen, digitalen Strukturen. Unser Anspruch ist es, Immobilienverwaltung transparent, zuverlässig und zeitgemäß zu gestalten — ohne anonyme Abläufe, unnötige Bürokratie oder das Gefühl, als Eigentümer nicht gehört zu werden.</p>
      <p>Wir wissen aus eigener Erfahrung, welche Verantwortung mit Immobilieneigentum verbunden ist. Als Eigentümer von Immobilien kennen wir die Fragen, Sorgen und Entscheidungen, die im Alltag entstehen: Sind die Kosten nachvollziehbar? Wird der Wert der Immobilie langfristig erhalten? Werden Probleme rechtzeitig erkannt? Ist im entscheidenden Moment ein verlässlicher Ansprechpartner erreichbar? Diese Perspektive prägt unsere tägliche Arbeit.</p>
      <p>Wir betrachten jede Immobilie so, als wäre sie unsere eigene. Das bedeutet für uns, verantwortungsvoll mit Geldern umzugehen, Entscheidungen wirtschaftlich abzuwägen und gleichzeitig den langfristigen Zustand sowie die Entwicklung der Immobilie im Blick zu behalten.</p>

      <h3>Persönlich erreichbar. Digital organisiert.</h3>
      <p>Moderne Immobilienverwaltung muss heute effizient, transparent und flexibel sein. Deshalb setzen wir auf digitale Prozesse, aktuelle Arbeitsweisen und klare Kommunikation. Dokumente, Vorgänge und wichtige Informationen werden strukturiert bearbeitet, sodass Entscheidungen nachvollziehbar bleiben und Anliegen nicht verloren gehen.</p>
      <p>Digitalisierung bedeutet für uns jedoch nicht, den persönlichen Kontakt zu ersetzen. Im Gegenteil: Moderne Systeme schaffen die nötige Zeit, um sich intensiver um die Immobilie und die Anliegen unserer Kunden kümmern zu können.</p>
      <p>Bei uns gibt es keine Verwaltung nach Schema F. Jede Immobilie, jede Eigentümergemeinschaft und jeder Eigentümer bringt individuelle Anforderungen mit. Wir hören zu, analysieren die Situation und entwickeln Lösungen, die zum Objekt und zu den Menschen passen.</p>

      <h3>Vertrauen entsteht durch Transparenz.</h3>
      <p>Eine gute Zusammenarbeit beginnt mit offener Kommunikation. Deshalb legen wir großen Wert auf verständliche Abrechnungen, nachvollziehbare Entscheidungen und klare Aussagen. Probleme werden nicht verschoben oder beschönigt, sondern frühzeitig angesprochen und lösungsorientiert bearbeitet.</p>
      <p>Unser Ziel ist eine Zusammenarbeit, bei der Eigentümer jederzeit wissen, dass ihre Immobilie fachlich kompetent, wirtschaftlich sinnvoll und mit persönlichem Engagement betreut wird.</p>
      <p>Wir möchten nicht nur verwalten. Wir möchten entlasten, Werte erhalten und gemeinsam mit unseren Kunden die Zukunft ihrer Immobilien gestalten.</p>
      <p class="prose-lead-out"><strong>HEINAND Immobilien steht für eine moderne Immobilienverwaltung, die digital denkt, persönlich handelt und Verantwortung übernimmt.</strong></p>
    </div>
  </div>
</section>

<section class="section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Unsere Haltung</span>
      <h2>Vertrauen entsteht durch klare Prozesse — nicht durch Versprechen.</h2>
    </div>
    <div style="max-width:760px;margin:0 auto 20px;text-align:center;">
      <p style="color:#5b6472;margin-bottom:16px;">Viele Eigentümer haben Verwaltung als Blackbox erlebt: Anrufe, die ins Leere laufen. Abrechnungen, die niemand versteht. Reparaturen, die Monate dauern. Genau deshalb gibt es HEINAND.</p>
      <p style="color:#5b6472;margin-bottom:16px;">Wir haben Verwaltung von Grund auf strukturiert aufgebaut: Jede Meldung wird erfasst und priorisiert, jeder Vorgang dokumentiert, jede Abrechnung nachvollziehbar aufbereitet. Dazu ein regionales Netzwerk aus Handwerkern und Dienstleistern, mit denen wir seit Jahren arbeiten.</p>
      <p style="color:#5b6472;">Das Ergebnis: Eigentümer, die ihre Immobilie wieder als Vermögenswert erleben — und nicht als zweiten Job.</p>
    </div>
    <div class="feature-grid" style="margin-top:48px;">
      {feature("bolt", "Digital", "Wir arbeiten vollständig digital: Anliegen kommen online rein, Vorgänge laufen im System. So sind wir bei jedem Objekt auf dem aktuellen Stand — und klären schnell statt zu suchen.")}
      {feature("check", "Strukturiert", "Jeder Vorgang folgt einem klaren Prozess: aufgenommen, priorisiert, erledigt, dokumentiert. Nichts bleibt liegen, nichts geht verloren.")}
      {feature("chart", "Transparent", "Digitale Vorgangsverwaltung und regelmäßiges Reporting: Sie wissen jederzeit, was mit Ihrer Immobilie passiert und was es kostet.")}
      {feature("pin", "Regional", "Wir verwalten nur, wo wir schnell vor Ort sind — in Mainz und Umgebung. Das ist keine Einschränkung, sondern unser Qualitätsversprechen.")}
    </div>
  </div>
</section>

<section class="section-white">
  <div class="container" style="text-align:center;">
    <h2 style="max-width:600px;margin:0 auto 24px;">Lernen Sie uns kennen — bei einem Kaffee in Mainz oder direkt an Ihrem Objekt.</h2>
    <a href="{prefix}kontakt.html" class="btn btn-primary">Erstgespräch vereinbaren</a>
  </div>
</section>

{cta_banner(prefix, "Sie möchten wissen, wie wir arbeiten?", "Im kostenlosen Erstgespräch zeigen wir Ihnen konkret, wie die Betreuung Ihres Objekts bei uns aussehen würde — mit Prozessen, digitaler Vorgangsverwaltung und transparenter Kostenstruktur.")}
'''
    write("ueber-uns.html", page(
        "Über uns — Hausverwaltung Mainz & Rhein-Main | HEINAND",
        "7 Jahre Erfahrung in der Immobilienverwaltung in Mainz, Wiesbaden und im 35-km-Umkreis. Digitale Prozesse, schnelle Klärung, volle Transparenz.",
        prefix, "ueber-uns", body, relpath="ueber-uns.html"
    ))

build_ueber_uns()
print("ueber-uns done")

# ==========================================================================
# KONTAKT
# ==========================================================================

def build_kontakt():
    prefix = ""
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Kontakt</span>
    <h1>Lassen Sie uns über Ihre Immobilie sprechen — kostenlos und unverbindlich.</h1>
    <p class="hero-lead">Schreiben Sie uns eine Nachricht oder buchen Sie direkt einen Termin für Ihr kostenloses Erstgespräch — telefonisch, per Video oder direkt an Ihrem Objekt.</p>
  </div>
</section>

<section class="section-white">
  <div class="container two-col">
    <div id="termin" class="form-card contact-tabs">
      <div class="tab-switch" role="tablist">
        <button type="button" class="tab-btn active" data-tab="message" role="tab" aria-selected="true">Nachricht senden</button>
        <button type="button" class="tab-btn" data-tab="booking" role="tab" aria-selected="false">Termin buchen</button>
      </div>

      <div class="tab-panel active" data-tab-panel="message">
        <form data-contact-form data-form-name="Kontaktformular">
          <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
          <div class="form-grid">
            {text_field("Ihr Name", "", True)}
            {text_field("E-Mail", "", True)}
            {text_field("Telefon (optional)", "", False)}
            {select_field("Ihr Anliegen", ["Mietverwaltung anfragen", "WEG-Verwaltung anfragen", "Sondereigentumsverwaltung", "Immobilie verkaufen", "Immobilie bewerten lassen", "Sonstiges Anliegen"])}
          </div>
          <div class="form-field full">
            <label>Ihre Nachricht *</label>
            <textarea rows="5"></textarea>
          </div>
          <button type="submit" class="btn btn-primary form-submit">Nachricht senden</button>
          <p class="form-note">Mit dem Absenden erklären Sie sich mit der Verarbeitung Ihrer Daten zur Bearbeitung der Anfrage einverstanden. Details in der <a href="{prefix}datenschutz.html">Datenschutzerklärung</a>.</p>
        </form>
      </div>

      <div class="tab-panel" data-tab-panel="booking">
        <p style="color:#5b6472;font-size:14px;margin-bottom:16px;">Wählen Sie direkt einen freien Termin für Ihr kostenloses Erstgespräch — die Buchung erfolgt über unseren Kalender und wird sofort bestätigt.</p>
        <div id="cal-heinand-inline" class="cal-embed"></div>
      </div>
    </div>
    <div>
      <span class="eyebrow">Direkt erreichen</span>
      <div class="contact-info-list" style="margin-top:20px;">
        <div class="contact-info-item">{contact_icon("phone")}<div><strong>{PHONE}</strong><span>Mo–Fr, 9–17 Uhr</span></div></div>
        <div class="contact-info-item">{contact_icon("mail")}<div><strong>{EMAIL}</strong><span>Antwort innerhalb eines Werktags</span></div></div>
        <div class="contact-info-item">{contact_icon("pin")}<div><strong>Menimaneweg 4, 55130 Mainz</strong><span>Termine nach Vereinbarung</span></div></div>
      </div>
      <span class="eyebrow">So läuft das Erstgespräch</span>
      <ol class="process-list" style="margin-top:16px;list-style:none;padding:0;">
        <li><span class="step-num" style="font-size:20px;margin-right:8px;">1.</span><span><b>Kennenlernen:</b> Telefonisch, bei uns in Mainz oder direkt an Ihrem Objekt.</span></li>
        <li><span class="step-num" style="font-size:20px;margin-right:8px;">2.</span><span><b>Objektanalyse:</b> Wir schauen uns Unterlagen, Zustand und Ihre Ziele an.</span></li>
        <li><span class="step-num" style="font-size:20px;margin-right:8px;">3.</span><span><b>Transparentes Angebot:</b> Sie erhalten einen konkreten Vorschlag — ohne Verpflichtung.</span></li>
      </ol>
    </div>
  </div>
</section>

<script type="text/javascript">
  (function (C, A, L) {{
    let p = function (a, ar) {{ a.q.push(ar); }};
    let d = C.document;
    C.Cal = C.Cal || function () {{
      let cal = C.Cal;
      let ar = arguments;
      if (!cal.loaded) {{
        cal.ns = {{}};
        cal.q = cal.q || [];
        d.head.appendChild(d.createElement("script")).src = A;
        cal.loaded = true;
      }}
      if (ar[0] === L) {{
        const api = function () {{ p(api, arguments); }};
        const namespace = ar[1];
        api.q = api.q || [];
        if (typeof namespace === "string") {{
          cal.ns[namespace] = cal.ns[namespace] || api;
          p(cal.ns[namespace], ar);
          p(cal, ["initNamespace", namespace]);
        }} else p(cal, ar);
        return;
      }}
      p(cal, ar);
    }};
  }})(window, "https://app.cal.com/embed/embed.js", "init");

  Cal("init", "heinand-termin", {{origin: "https://cal.com"}});

  Cal.ns["heinand-termin"]("inline", {{
    elementOrSelector: "#cal-heinand-inline",
    calLink: "heinand-immobilien",
    layout: "month_view",
  }});

  Cal.ns["heinand-termin"]("ui", {{
    theme: "light",
    hideEventTypeDetails: false,
    layout: "month_view",
    styles: {{ branding: {{ brandColor: "#0f3063" }} }},
  }});
</script>
'''
    write("kontakt.html", page(
        "Kontakt — Erstgespräch vereinbaren | HEINAND",
        "Kontaktieren Sie HEINAND Immobilien in Mainz: kostenloses Erstgespräch zu Verwaltung oder Verkauf. Wir melden uns innerhalb eines Werktags.",
        prefix, "kontakt", body, relpath="kontakt.html"
    ))

build_kontakt()
print("kontakt done")

# ==========================================================================
# SCHADENSMELDUNG
# ==========================================================================

def build_schadensmeldung():
    prefix = ""
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Schadensmeldung</span>
    <h1>Schaden melden — in zwei Minuten erledigt.</h1>
    <p class="hero-lead">Damit wir schnell und richtig reagieren können: Wählen Sie die passende Schadensart, wir stufen die Dringlichkeit automatisch ein — den Rest übernehmen wir.</p>
  </div>
</section>

<section class="section-white">
  <div class="container" style="max-width:780px;">
    <form class="form-card" data-contact-form data-form-name="Schadensmeldung">
      <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
      <div class="form-step-label" style="margin-top:0;">1. Um welche Art von Schaden handelt es sich?</div>

      <div class="form-field">
        <label>Schadensart *</label>
        <select id="schadensart" name="schadensart" required>
          <option value="" disabled selected>Bitte wählen …</option>
          <optgroup label="Akute Gefahr">
            <option data-priority="akut">Wasserschaden / Rohrbruch</option>
            <option data-priority="akut">Stromausfall (gesamte Wohnung/Gebäude)</option>
            <option data-priority="akut">Gasgeruch / Gasleck</option>
            <option data-priority="akut">Tür lässt sich nicht mehr verschließen / Einbruch</option>
            <option data-priority="akut">Brand- oder Rauchschaden</option>
            <option data-priority="akut">Sturmschaden mit akuter Gefährdung</option>
          </optgroup>
          <optgroup label="Dringend">
            <option data-priority="dringend">Heizungsausfall</option>
            <option data-priority="dringend">Undichtes Fenster</option>
            <option data-priority="dringend">Ausfall Warmwasser</option>
            <option data-priority="dringend">Feuchtigkeitsschaden / Wasserfleck an Decke oder Wand</option>
            <option data-priority="dringend">Verstopfter Abfluss mit Rückstau</option>
            <option data-priority="dringend">Defekte Wohnungs- oder Haustür (Schließmechanismus)</option>
            <option data-priority="dringend">Schädlingsbefall</option>
          </optgroup>
          <optgroup label="Regulär">
            <option data-priority="regulaer">Klemmende Tür</option>
            <option data-priority="regulaer">Tropfender Wasserhahn</option>
            <option data-priority="regulaer">Fenster schließt schwer</option>
            <option data-priority="regulaer">Defekter Lichtschalter oder Steckdose</option>
            <option data-priority="regulaer">Rollladen defekt</option>
            <option data-priority="regulaer">Klingel- oder Gegensprechanlage defekt</option>
            <option data-priority="regulaer">Kosmetischer Mangel (Wand, Boden, Anstrich)</option>
          </optgroup>
          <option value="sonstige" data-priority="unbekannt">Sonstiges (bitte unten beschreiben)</option>
        </select>
      </div>

      <div class="priority-indicator" id="priorityIndicator" hidden>
        <strong id="priorityTitle"></strong>
        <span class="desc" id="priorityDesc"></span>
        <span class="impact" id="priorityImpact"></span>
      </div>

      <div class="form-step-label">2. Wer meldet und wo?</div>
      <div class="form-grid">
        <div class="form-field">
          <label>Vorname *</label>
          <input type="text" placeholder="Max" required>
        </div>
        <div class="form-field">
          <label>Nachname *</label>
          <input type="text" placeholder="Mustermann" required>
        </div>
      </div>
      <div class="form-grid">
        <div class="form-field">
          <label>Telefonnummer *</label>
          <input type="tel" placeholder="Für Rückfragen" required>
        </div>
        <div class="form-field">
          <label>E-Mail *</label>
          <input type="email" placeholder="Für die Bestätigung" required>
        </div>
      </div>
      <div class="form-grid">
        <div class="form-field">
          <label>Objektadresse *</label>
          <input type="text" placeholder="Straße, Hausnummer, PLZ, Ort" required>
        </div>
        <div class="form-field">
          <label>Wohneinheit *</label>
          <input type="text" placeholder="z. B. 2. OG rechts, WE 4" required>
        </div>
      </div>

      <div class="form-step-label">3. Was ist passiert?</div>
      <div class="form-field">
        <label class="sr-only">Schadensbeschreibung</label>
        <textarea rows="5" placeholder="Beschreiben Sie den Schaden so konkret wie möglich: Was, wo, seit wann? Ist bereits etwas unternommen worden?" required></textarea>
      </div>

      <div class="form-step-label">4. Fotos hinzufügen (optional)</div>
      <div class="form-field">
        <label for="schadenFotos">Fotos vom Schaden</label>
        <input type="file" id="schadenFotos" accept="image/*" multiple>
        <span class="form-hint">Bis zu 5 Fotos (JPG/PNG) — hilft uns, den Schaden vorab besser einzuschätzen.</span>
      </div>

      <button type="submit" class="btn btn-primary form-submit">Schaden melden</button>
    </form>
  </div>
</section>
'''
    write("schadensmeldung.html", page(
        "Schaden melden — Online-Schadensmeldung | HEINAND",
        "Schaden online melden bei HEINAND Immobilien: Schadensart auswählen, Dringlichkeit wird automatisch erkannt — schnelle, priorisierte Bearbeitung.",
        prefix, "", body, relpath="schadensmeldung.html"
    ))

build_schadensmeldung()
print("schadensmeldung done")

# ==========================================================================
# IMPRESSUM / DATENSCHUTZ
# ==========================================================================

def build_impressum():
    prefix = ""
    body = f'''
<section class="hero hero-page" style="padding-bottom:60px;">
  <div class="container hero-inner"><h1 style="font-size:38px;">Impressum</h1></div>
</section>
<section class="section-white">
  <div class="container legal">
    <h2>Angaben gemäß § 5 DDG</h2>
    <p>HEINAND Immobilien<br>Inhaber: Philipp Hartung (Einzelunternehmen)<br>Menimaneweg 4<br>55130 Mainz</p>

    <h2>Kontakt</h2>
    <p>Telefon: {PHONE}<br>E-Mail: {EMAIL}</p>

    <h2>Erlaubnis nach § 34c GewO</h2>
    <p>Gewerbeerlaubnis als Wohnimmobilienverwalter nach § 34c Abs. 1 Satz 1 Nr. 4 Gewerbeordnung (GewO).<br>
    Zuständige Erlaubnis- und Aufsichtsbehörde: <span class="placeholder">[Einfügen erforderlich — zuständige Behörde am Geschäftssitz]</span></p>

    <h2>Berufshaftpflichtversicherung</h2>
    <p class="placeholder">[Einfügen erforderlich — Name und Sitz des Versicherers, räumlicher Geltungsbereich (Pflichtversicherung für Wohnimmobilienverwalter gemäß § 34c Abs. 2a GewO i. V. m. § 15 MaBV)]</p>

    <h2>Umsatzsteuer-ID</h2>
    <p class="placeholder">[Einfügen erforderlich]</p>

    <h2>Verbraucherstreitbeilegung</h2>
    <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

    <div class="notice-box">Hinweis: Vor dem Go-Live noch ergänzen — echte Geschäftsanschrift, zuständige Erlaubnisbehörde (§ 34c GewO), Berufshaftpflichtversicherer sowie USt-ID bzw. Steuernummer.</div>
  </div>
</section>
'''
    write("impressum.html", page("Impressum | HEINAND Immobilien",
        "Impressum von HEINAND Immobilien — Miet-, WEG- und Sondereigentumsverwaltung sowie Immobilienverkauf in Mainz und dem Rhein-Main-Gebiet.",
        prefix, "", body, relpath="impressum.html", noindex=True))

def build_datenschutz():
    prefix = ""
    body = f'''
<section class="hero hero-page" style="padding-bottom:60px;">
  <div class="container hero-inner"><h1 style="font-size:38px;">Datenschutzerklärung</h1></div>
</section>
<section class="section-white">
  <div class="container legal">
    <h2>Verantwortlicher</h2>
    <p>HEINAND Immobilien, Menimaneweg 4, 55130 Mainz — {EMAIL}</p>

    <h2>Datenverarbeitung auf dieser Website</h2>
    <p>Beim Besuch werden durch den Hosting-Anbieter technisch notwendige Server-Logdaten (IP-Adresse, Zeitpunkt, aufgerufene Seite) verarbeitet — Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einem sicheren Betrieb).</p>

    <h2>Cookies & Besucher-Statistik</h2>
    <p>Technisch notwendige Cookies (z. B. zur Speicherung Ihrer Cookie-Entscheidung) setzen wir auf Grundlage von § 25 Abs. 2 TDDDG. Nur mit Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG) verwenden wir zusätzlich eine eigene, anonyme Besucher-Statistik: ein Zufalls-Cookie („hn_vid“, 12 Monate) und die Zählung von Seitenaufrufen auf unseren eigenen Servern. Es kommen keine Drittanbieter-Dienste und kein Werbe-Tracking zum Einsatz. Ihre Einwilligung können Sie jederzeit über „Cookie-Einstellungen“ im Fußbereich widerrufen.</p>

    <h2>Kontaktaufnahme</h2>
    <p>Wenn Sie uns per Formular, E-Mail oder Telefon kontaktieren, verarbeiten wir die von Ihnen mitgeteilten Daten zur Bearbeitung Ihrer Anfrage (Art. 6 Abs. 1 lit. b DSGVO). Die Daten werden gelöscht, sobald sie für die Bearbeitung nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>

    <h2>Ihre Rechte</h2>
    <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit sowie Widerspruch (Art. 15–21 DSGVO) und das Recht auf Beschwerde bei einer Aufsichtsbehörde.</p>

    <div class="notice-box">Hinweis: Platzhalter-Datenschutzerklärung. Vor dem Go-Live juristisch prüfen und an das finale Hosting-Setup (z. B. Vercel, Fonts, ggf. Formular-Backend) anpassen.</div>
  </div>
</section>
'''
    write("datenschutz.html", page("Datenschutzerklärung | HEINAND Immobilien",
        "Datenschutzerklärung von HEINAND Immobilien — Miet-, WEG- und Sondereigentumsverwaltung sowie Immobilienverkauf in Mainz und dem Rhein-Main-Gebiet.",
        prefix, "", body, relpath="datenschutz.html", noindex=True))

build_impressum()
build_datenschutz()
print("legal done")

# ==========================================================================
# BLOG
# ==========================================================================

ARTICLES = [
    dict(slug="weg-verwaltung-wechseln", tag="WEG", date="15. Juni 2026", read="6 Min.",
         title="WEG-Verwaltung wechseln: So gelingt der Verwalterwechsel Schritt für Schritt",
         seo_title="WEG-Verwaltung wechseln: So geht's",
         teaser="Unzufrieden mit der Hausverwaltung? So wechselt Ihre WEG den Verwalter: Fristen, Beschluss, Übergabe — inkl. Checkliste für Mainz & Rhein-Main.",
         related_service=("WEG-Verwaltung", "leistungen/weg-verwaltung.html", "Verwaltung für Wohnungseigentümergemeinschaften — rechtssicher und transparent."),
         html='''
<p>Nicht erreichbar, Abrechnungen zu spät, Beschlüsse bleiben liegen: Wenn die Verwaltung nicht funktioniert, leidet die ganze Eigentümergemeinschaft. Die gute Nachricht: Ein Verwalterwechsel ist einfacher, als viele denken — wenn er strukturiert angegangen wird.</p>

<h2>Wann ist ein Verwalterwechsel sinnvoll?</h2>
<p>Nicht jede Unzufriedenheit rechtfertigt gleich einen Wechsel. Es gibt aber klare Warnsignale, bei denen Eigentümergemeinschaften handeln sollten:</p>
<ul>
<li>Jahresabrechnung und Wirtschaftsplan kommen regelmäßig zu spät oder sind fehlerhaft</li>
<li>Beschlüsse aus Eigentümerversammlungen werden nicht oder nur schleppend umgesetzt</li>
<li>Die Verwaltung ist für Eigentümer und Beirat schlecht bis gar nicht erreichbar</li>
<li>Instandhaltungsmaßnahmen werden verschleppt, das Objekt verliert sichtbar an Zustand</li>
<li>Es fehlt jede Transparenz über Kosten, Aufträge und laufende Vorgänge</li>
</ul>

<h2>Die rechtliche Grundlage: Bestellung und Abberufung</h2>
<p>Seit der WEG-Reform kann der Verwalter jederzeit abberufen werden — ein wichtiger Grund ist nicht mehr erforderlich. Der Verwaltervertrag endet dann spätestens sechs Monate nach der Abberufung. Für den Wechsel braucht es einen Mehrheitsbeschluss der Eigentümerversammlung.</p>
<p>Praktisch heißt das: Die Gemeinschaft sammelt Angebote neuer Verwaltungen, setzt den Punkt auf die Tagesordnung der nächsten Versammlung (oder beruft eine außerordentliche ein) und beschließt Abberufung und Neubestellung idealerweise im selben Termin.</p>

<h2>Der Ablauf in fünf Schritten</h2>
<p>So läuft ein sauberer Verwalterwechsel in der Praxis ab:</p>
<ul>
<li>1. Angebote einholen: Zwei bis drei Verwaltungen anfragen, Leistungskatalog und Kosten vergleichen</li>
<li>2. Kandidaten prüfen: Referenzen, regionale Präsenz, Erreichbarkeit und digitale Prozesse hinterfragen</li>
<li>3. Beschluss fassen: Abberufung der alten und Bestellung der neuen Verwaltung in der Eigentümerversammlung</li>
<li>4. Übergabe organisieren: Unterlagen, Konten, Verträge und laufende Vorgänge — das übernimmt die neue Verwaltung</li>
<li>5. Kommunikation: Eigentümer, Mieter und Dienstleister über den Wechsel informieren</li>
</ul>

<h2>Worauf Sie bei der neuen Verwaltung achten sollten</h2>
<p>Der häufigste Fehler beim Wechsel: Es wird nur auf den Preis geschaut. Eine Verwaltung, die pro Einheit zwei Euro günstiger ist, aber Abrechnungen verspätet liefert und Beschlüsse nicht umsetzt, kostet die Gemeinschaft am Ende deutlich mehr.</p>
<p>Entscheidend sind stattdessen: eine digitale Vorgangsverwaltung, nachvollziehbare Prozesse für Schadensmeldungen und Beschlussumsetzung, schnelle Rückmeldungen und regionale Präsenz für kurzfristige Objekttermine.</p>

<h2>Fazit</h2>
<p>Ein Verwalterwechsel ist kein Hexenwerk: Mehrheitsbeschluss, saubere Übergabe, klare Kommunikation. Wichtig ist, dass die neue Verwaltung die Übernahme strukturiert führt — dann merken Eigentümer vom Wechsel vor allem eines: dass es endlich funktioniert.</p>
'''),
    dict(slug="nebenkostenabrechnung-fehler", tag="Vermietung", date="28. Mai 2026", read="7 Min.",
         title="Nebenkostenabrechnung: Die 7 häufigsten Fehler — und wie Vermieter sie vermeiden",
         seo_title="Nebenkostenabrechnung: 7 häufige Fehler",
         teaser="Formfehler, verpasste Fristen, falsche Umlageschlüssel: Die 7 häufigsten Fehler in der Nebenkostenabrechnung und wie private Vermieter sie sicher vermeiden.",
         related_service=("Mietverwaltung", "leistungen/mietverwaltung.html", "Komplette Betreuung Ihrer Mietobjekte — von der Korrespondenz bis zur Abrechnung."),
         html='''
<p>Die Betriebskostenabrechnung ist die häufigste Streitquelle zwischen Vermietern und Mietern — und die häufigste Fehlerquelle für private Vermieter. Wer hier Formfehler macht, verliert im Zweifel bares Geld: Nachforderungen verfallen, Kürzungen drohen.</p>

<h2>Fehler 1: Die Abrechnungsfrist verpassen</h2>
<p>Die wichtigste Regel: Die Abrechnung muss dem Mieter spätestens zwölf Monate nach Ende des Abrechnungszeitraums zugehen. Wer die Frist verpasst, kann Nachzahlungen nicht mehr verlangen — Guthaben muss er trotzdem auszahlen. Für das Abrechnungsjahr 2025 heißt das: Zugang beim Mieter bis 31.12.2026.</p>

<h2>Fehler 2: Nicht umlagefähige Kosten abrechnen</h2>
<p>Umlagefähig ist nur, was die Betriebskostenverordnung (BetrKV) erlaubt und was im Mietvertrag vereinbart wurde. Klassische Fehlgriffe:</p>
<ul>
<li>Instandhaltung und Reparaturen (nicht umlagefähig)</li>
<li>Verwaltungskosten (nicht umlagefähig)</li>
<li>Bankgebühren, Porto, Leerstandskosten (trägt der Eigentümer)</li>
<li>Einmalige Anschaffungen statt laufender Kosten</li>
</ul>

<h2>Fehler 3: Falscher oder wechselnder Umlageschlüssel</h2>
<p>Ohne vertragliche Regelung gilt die Wohnfläche als Umlageschlüssel. Wer stattdessen nach Personenzahl oder Einheiten verteilt — oder den Schlüssel von Jahr zu Jahr wechselt — produziert eine angreifbare Abrechnung. Ausnahme: verbrauchsabhängige Kosten wie Heizung und Warmwasser, die nach Heizkostenverordnung überwiegend nach Verbrauch abgerechnet werden müssen.</p>

<h2>Fehler 4–7: Form, Belege, Vorauszahlungen, WEG-Abrechnung</h2>
<p>Vier weitere Stolperfallen, die in der Praxis regelmäßig zu Kürzungen führen:</p>
<ul>
<li>Formfehler: Die Abrechnung muss Gesamtkosten, Umlageschlüssel, Anteil des Mieters und Vorauszahlungen nachvollziehbar ausweisen</li>
<li>Fehlende Belegeinsicht: Mieter haben das Recht, Originalbelege einzusehen — wer sie nicht vorlegen kann, riskiert Kürzungen</li>
<li>Vorauszahlungen falsch verrechnet: Ist-Zahlungen zählen, nicht Soll-Zahlungen</li>
<li>WEG-Hausgeldabrechnung 1:1 übernommen: Die Jahresabrechnung der WEG enthält nicht umlagefähige Positionen — sie muss für Mieter aufbereitet werden</li>
</ul>

<h2>Fazit</h2>
<p>Eine korrekte Nebenkostenabrechnung ist Handwerk: richtige Frist, richtige Kosten, richtiger Schlüssel, richtige Form. Wer mehrere Einheiten verwaltet, unterschätzt den Aufwand schnell — und zahlt Fehler direkt aus eigener Tasche. Eine professionelle Mietverwaltung rechnet fristgerecht, rechtssicher und nachvollziehbar ab.</p>
'''),
    dict(slug="immobilie-verkaufen-mainz", tag="Verkauf", date="10. Mai 2026", read="6 Min.",
         title="Immobilie verkaufen in Mainz: Marktlage, Ablauf und die größten Preisfehler",
         seo_title="Immobilie verkaufen in Mainz",
         teaser="Immobilienverkauf in Mainz & Rhein-Main: Wie Sie den richtigen Angebotspreis finden, welche Unterlagen Sie brauchen und welche Fehler Verkäufer Geld kosten.",
         related_service=("Immobilienverkauf", "leistungen/immobilienverkauf.html", "Vom Exposé bis zum Notartermin — Verkauf mit regionaler Marktkenntnis."),
         html='''
<p>Mainz gehört zu den stabilsten Wohnimmobilienmärkten in Rheinland-Pfalz: Universitätsstadt, Landeshauptstadt, Pendlerlage ins Rhein-Main-Gebiet. Wer hier verkauft, verkauft in einen Nachfragemarkt — und verschenkt trotzdem oft Geld. Meist aus zwei Gründen: falscher Preis oder schlechte Vorbereitung.</p>

<h2>Der größte Fehler: der falsche Angebotspreis</h2>
<p>Zu hoch angesetzte Immobilien "verbrennen" am Markt: Sie liegen monatelang in den Portalen, Interessenten werden misstrauisch, und am Ende wird unter Wert verkauft. Zu niedrig angesetzte Objekte verschenken direkt Geld.</p>
<p>Die Lösung ist eine fundierte Werteinschätzung auf Basis echter Vergleichsdaten aus der Region — nicht der Online-Rechner und nicht der Nachbar, der "gehört hat, was nebenan bezahlt wurde".</p>

<h2>Diese Unterlagen brauchen Sie</h2>
<p>Käufer und deren Banken erwarten heute vollständige Unterlagen. Dazu gehören:</p>
<ul>
<li>Grundbuchauszug (aktuell)</li>
<li>Energieausweis (Pflicht bereits für die Anzeige!)</li>
<li>Grundrisse, Wohnflächenberechnung, Baubeschreibung</li>
<li>Bei Eigentumswohnungen: Teilungserklärung, Protokolle der letzten Eigentümerversammlungen, Hausgeldabrechnungen, Stand der Erhaltungsrücklage</li>
<li>Bei vermieteten Objekten: Mietverträge und aktuelle Mietaufstellung</li>
</ul>

<h2>Der Ablauf: von der Bewertung bis zum Notartermin</h2>
<p>Ein strukturierter Verkauf läuft in klaren Etappen: Werteinschätzung und Preisstrategie, Aufbereitung von Exposé und Unterlagen, gezielte Vermarktung, vorqualifizierte Besichtigungen, Bonitätsprüfung der Kaufinteressenten, Verhandlung, Kaufvertragsabstimmung und Notartermin.</p>
<p>Gerade die Bonitätsprüfung wird von Privatverkäufern oft übersprungen — und genau dort platzen Verkäufe: nach Monaten, kurz vor dem Notartermin, weil die Finanzierung nicht steht.</p>

<h2>Vermietet verkaufen — Chance statt Problem</h2>
<p>Eine vermietete Wohnung schreckt Selbstnutzer ab, ist für Kapitalanleger aber genau richtig. Entscheidend ist, die richtige Käufergruppe anzusprechen: Mit sauber dokumentierten Mietverhältnissen, nachvollziehbarer Rendite und geordneter Verwaltung wird ein vermietetes Objekt zum Anlageprodukt — und erzielt oft bessere Preise als gedacht.</p>

<h2>Fazit</h2>
<p>In Mainz zu verkaufen ist keine Kunst — zum besten Preis zu verkaufen schon. Realistische Bewertung, vollständige Unterlagen, geprüfte Käufer: Wer diese drei Punkte ernst nimmt, verkauft schneller und besser. Ein regionaler Partner mit Verwalter-Know-how kennt dabei beide Seiten: das Objekt und den Markt.</p>
'''),
    dict(slug="hausverwaltung-kosten", tag="Eigentümerwissen", date="20. April 2026", read="5 Min.",
         title="Was kostet eine Hausverwaltung? Preise, Modelle und woran Sie Qualität erkennen",
         seo_title="Was kostet eine Hausverwaltung?",
         teaser="Was kostet eine Hausverwaltung pro Wohneinheit? Übliche Preisspannen für Miet-, WEG- und SE-Verwaltung — und warum billig oft teuer wird.",
         related_service=("Mietverwaltung", "leistungen/mietverwaltung.html", "Komplette Betreuung Ihrer Mietobjekte — von der Korrespondenz bis zur Abrechnung."),
         html='''
<p>Die Frage nach den Kosten ist meist die erste — und die am häufigsten falsch gestellte. Denn entscheidend ist nicht, was eine Verwaltung pro Monat kostet, sondern was sie Ihnen erspart: an Zeit, an Fehlern und an Wertverlust.</p>

<h2>Übliche Preismodelle im Überblick</h2>
<p>Hausverwaltungen rechnen in der Regel pro Einheit und Monat ab. Die Spannen unterscheiden sich je nach Leistungsart:</p>
<ul>
<li>Mietverwaltung: meist prozentual von der Nettokaltmiete oder als Festbetrag pro Einheit</li>
<li>WEG-Verwaltung: Festbetrag pro Einheit und Monat, abhängig von Objektgröße und Zustand</li>
<li>Sondereigentumsverwaltung: Festbetrag pro Wohnung, oft kombinierbar mit der WEG-Verwaltung</li>
<li>Zusatzleistungen: Neuvermietung, Versammlungen außer der Reihe oder Bauüberwachung werden separat vereinbart</li>
</ul>

<h2>Warum "billig" oft teuer wird</h2>
<p>Eine Verwaltung, die kaum kostendeckend kalkuliert, muss an der Betreuung sparen: keine Objektbegehungen, langsame Reaktion, Standardabrechnungen ohne Prüfung. Die Folgekosten tragen Eigentümer — als Reparaturstau, fehlerhafte Abrechnungen oder Leerstand.</p>
<p>Die richtige Frage ist deshalb nicht "Was kostet die Verwaltung?", sondern "Was bekomme ich dafür?" Ein transparenter Leistungskatalog ist wichtiger als der letzte Euro Preisunterschied.</p>

<h2>Woran Sie eine gute Verwaltung erkennen</h2>
<p>Qualitätsmerkmale, die Sie vor Vertragsschluss prüfen sollten:</p>
<ul>
<li>Digitale Arbeitsweise: Anliegen werden erfasst und geklärt statt vergessen</li>
<li>Klar definierte Reaktionszeiten, besonders für Notfälle</li>
<li>Digitale Vorgangsverwaltung mit nachvollziehbarer Dokumentation</li>
<li>Regionale Präsenz für schnelle Objekttermine</li>
<li>Transparenter Leistungskatalog: Was ist inklusive, was kostet extra?</li>
</ul>

<h2>Fazit</h2>
<p>Verwaltungskosten sind gut investiert, wenn die Leistung stimmt: fristgerechte Abrechnungen, gepflegte Objekte, schnelle Rückmeldungen. Vergleichen Sie Leistungskataloge statt nur Preise — und lassen Sie sich ein konkretes Angebot für Ihr Objekt machen.</p>
'''),
    dict(slug="sondereigentumsverwaltung-kapitalanleger", tag="Eigentümerwissen", date="30. März 2026", read="5 Min.",
         title="Sondereigentumsverwaltung: Warum Kapitalanleger beides brauchen — WEG und SE",
         seo_title="SE-Verwaltung für Kapitalanleger",
         teaser="WEG-Verwaltung kümmert sich ums Haus, nicht um Ihre Wohnung: Was Sondereigentumsverwaltung leistet, was sie kostet und wann sie sich für Kapitalanleger rechnet.",
         related_service=("Sondereigentumsverwaltung", "leistungen/se-verwaltung.html", "Betreuung Ihrer Eigentumswohnung innerhalb der WEG — speziell für Kapitalanleger."),
         html='''
<p>Viele Wohnungskäufer glauben: "Das Haus hat doch eine Hausverwaltung, die kümmert sich." Ein teurer Irrtum — denn die WEG-Verwaltung ist nur für das Gemeinschaftseigentum zuständig. Um Mieter, Mietvertrag und Abrechnung Ihrer Wohnung kümmert sich: niemand. Außer Ihnen.</p>

<h2>WEG-Verwaltung vs. Sondereigentumsverwaltung</h2>
<p>Die Abgrenzung ist einfach, wenn man sie einmal verstanden hat: Die WEG-Verwaltung betreut alles, was allen gehört — Dach, Fassade, Treppenhaus, Heizungsanlage. Die Sondereigentumsverwaltung (SE-Verwaltung) betreut alles, was nur Ihnen gehört: Ihre Wohnung und Ihr Mietverhältnis.</p>
<ul>
<li>WEG-Verwaltung: Eigentümerversammlung, Hausgeld, Instandhaltung des Gemeinschaftseigentums</li>
<li>SE-Verwaltung: Mieterkontakt, Mietinkasso, Nebenkostenabrechnung, Reparaturen in der Wohnung, Neuvermietung</li>
</ul>

<h2>Für wen sich SE-Verwaltung rechnet</h2>
<p>Die SE-Verwaltung lohnt sich besonders für drei Gruppen: Kapitalanleger, die nicht am Objektstandort wohnen und keinen Mieterkontakt führen können oder wollen. Eigentümer mehrerer Wohnungen, bei denen der Verwaltungsaufwand in Summe erheblich ist. Und Erben, die plötzlich Vermieter sind, ohne es je geplant zu haben.</p>
<p>Der Rechenweg ist einfach: Was kostet Sie eine verpatzte Nebenkostenabrechnung, ein Mietausfall wegen schleppender Neuvermietung oder ein eskalierter Mieterkonflikt — verglichen mit dem monatlichen Festbetrag einer professionellen Betreuung?</p>

<h2>Der unterschätzte Vorteil: Ihre Stimme in der WEG</h2>
<p>Ein guter SE-Verwalter ist auch Ihre Schnittstelle zur Eigentümergemeinschaft: Er prüft Hausgeldabrechnungen, bereitet Versammlungen vor und nimmt auf Wunsch mit Vollmacht teil. Gerade für auswärtige Anleger heißt das: Ihre Interessen werden vertreten, auch wenn Sie nicht vor Ort sind.</p>

<h2>Fazit</h2>
<p>Wer eine vermietete Eigentumswohnung besitzt, braucht zwei Verwaltungsebenen: die WEG fürs Haus, die SE-Verwaltung für die eigene Wohnung. Aus einer Hand koordiniert, wird aus der Kapitalanlage das, was sie sein soll — ein Investment, kein Nebenjob.</p>
'''),
]

def build_blog_index():
    prefix = "../"  # links to root-level pages (used by header/footer/cta banner)
    cards = ""
    for a in ARTICLES:
        cards += f'''<a href="{a['slug']}.html" class="blog-card">
  <span class="tag"><img src="{prefix}assets/blog/{a['slug']}.png" alt="{a['title']}" loading="lazy"></span>
  <div>
    <span class="meta">{a['tag']} <span>· {a['date']} · {a['read']} Lesezeit</span></span>
    <h3>{a['title']}</h3>
    <p>{a['teaser']}</p>
  </div>
</a>'''
    body = f'''
<section class="hero hero-page">
  <div class="container hero-inner">
    <span class="eyebrow">Ratgeber</span>
    <h1>Wissen für Eigentümer — klar erklärt.</h1>
    <p class="hero-lead">Hausverwaltung, WEG-Recht, Vermietung und Verkauf: praxisnahes Wissen aus 7 Jahren Verwaltungsalltag in Mainz und Rhein-Main.</p>
  </div>
</section>
<section class="section-cream">
  <div class="container">
    <div class="blog-grid">{cards}</div>
  </div>
</section>
{cta_banner(prefix, "Lieber direkt fragen statt lange lesen?", "Im kostenlosen Erstgespräch beantworten wir Ihre Fragen konkret für Ihr Objekt — ohne Fachchinesisch und ohne Verpflichtung.")}
'''
    write("blog/index.html", page(
        "Ratgeber für Eigentümer & Vermieter | HEINAND Immobilien",
        "Der HEINAND-Ratgeber: fundiertes Wissen zu Hausverwaltung, WEG-Recht, Vermietung und Immobilienverkauf in Mainz & Rhein-Main — verständlich erklärt.",
        prefix, "blog", body, relpath="blog/index.html"
    ))

def build_article(a):
    prefix = "../"
    others = [x for x in ARTICLES if x["slug"] != a["slug"]][:2]
    related_html = "".join(f'''<a href="{prefix}blog/{o['slug']}.html"><span class="meta">{o['tag']} · {o['date']}</span><strong>{o['title']}</strong><span class="rd">Artikel lesen &#8594;</span></a>''' for o in others)
    sname, shref, sdesc = a["related_service"]
    body = f'''
<section class="hero hero-page" style="padding-bottom:56px;">
  <div class="container hero-inner article-header">
    <a href="{prefix}blog/index.html" style="color:var(--gold-light);font-size:14px;font-weight:600;">&#8592; Alle Artikel</a>
    <div style="margin-top:18px;">
      <span class="eyebrow">{a['tag']}</span>
      <span style="color:rgba(255,255,255,0.6);font-size:13px;margin-left:10px;">{a['date']} · {a['read']} Lesezeit</span>
    </div>
    <h1 style="font-size:36px;margin-top:14px;">{a['title']}</h1>
  </div>
</section>
<section class="section-white">
  <div class="container article-body">
    {a['html']}
    <div class="article-related-service">
      <span class="eyebrow">Passende Leistung</span>
      <h3>{sname}</h3>
      <p>{sdesc}</p>
      <a href="{prefix}{shref}" class="btn btn-navy">Mehr erfahren</a>
    </div>
  </div>
  <div class="container">
    <h3 style="text-align:center;margin-bottom:20px;font-size:22px;">Weiterlesen</h3>
    <div class="related-articles">{related_html}</div>
  </div>
</section>
{cta_banner(prefix)}
'''
    write(f"blog/{a['slug']}.html", page(
        f"{a.get('seo_title', a['title'])} | HEINAND Immobilien",
        a['teaser'],
        prefix, "blog", body, relpath=f"blog/{a['slug']}.html"
    ))

build_blog_index()
for a in ARTICLES:
    build_article(a)
print("blog done")

build_home()
print("home done")

# ==========================================================================
# SITEMAP.XML + ROBOTS.TXT
# ==========================================================================

def build_sitemap_and_robots():
    import glob as _glob
    from datetime import date
    # standorte/worms.html: gehört nicht mehr zum Einzugsgebiet und wird nicht mehr
    # verlinkt; falls die Datei im Build-Verzeichnis als Altlast liegen bleibt, aus
    # Sitemap/Index ausschließen.
    noindex_files = {"impressum.html", "datenschutz.html", "standorte/worms.html"}
    html_files = sorted(
        os.path.relpath(p, ROOT).replace(os.sep, "/")
        for p in _glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
    )
    today = date.today().isoformat()
    urls = []
    for relpath in html_files:
        if relpath in noindex_files:
            continue
        priority = "1.0" if relpath == "index.html" else ("0.8" if relpath.count("/") == 0 else "0.6")
        urls.append(
            f"  <url>\n    <loc>{DOMAIN}{canonical_path(relpath)}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n"
    )
    write("sitemap.xml", sitemap)

    robots = f'''User-agent: *
Allow: /
Disallow: /impressum.html
Disallow: /datenschutz.html

Sitemap: {DOMAIN}/sitemap.xml
'''
    write("robots.txt", robots)

build_sitemap_and_robots()
print("sitemap + robots done")

print("ALL PAGES GENERATED")
