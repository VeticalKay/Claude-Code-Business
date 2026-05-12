#!/usr/bin/env python3
"""
E-Mail Sortierer — Katarina Tolkmit
Sortiert beide Postfächer täglich automatisch in definierte Ordner.
Läuft täglich via Cron Job.
"""

import imaplib
import email
import email.policy
import os
import re
from email.header import decode_header

# ============================================================
# KONFIGURATION
# ============================================================

ENV_FILE = os.path.expanduser("~/.config/buchhaltung/.env")

def load_env(path):
    env = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
    except FileNotFoundError:
        print(f"WARNUNG: .env Datei nicht gefunden: {path}")
    return env

ENV = load_env(ENV_FILE)

ACCOUNTS = {
    "tolkmit": {
        "host": "imap.tng.de",
        "username": "ktolkmit",
        "password": ENV.get("TOLKMIT_PASSWORD", ""),
        "label": "katarina@tolkmit.de",
    },
    "verticalkay": {
        "host": "server1.codeking.at",
        "username": "office@verticalkay.de",
        "password": ENV.get("VERTICALKAY_PASSWORD", ""),
        "label": "office@verticalkay.de",
    },
}

# ============================================================
# ORDNERSTRUKTUR
# ============================================================

IMAP_PREFIX = "INBOX."
IMAP_SEP = "."

def imap_folder(logical_path):
    """Logischen Pfad (mit /) in IMAP-Pfad (INBOX. mit .) umwandeln."""
    return IMAP_PREFIX + logical_path.replace("/", IMAP_SEP)

TOLKMIT_FOLDERS = [
    imap_folder(f) for f in [
        "Rechnungen",
        "Rechnungen/PayPal",
        "Rechnungen/Apple",
        "Rechnungen/Adobe",
        "Rechnungen/Canva",
        "Rechnungen/Google",
        "Rechnungen/Zoom",
        "Rechnungen/Amazon",
        "Rechnungen/Eversports",
        "Rechnungen/Anthropic",
        "Rechnungen/Lagermax",
        "Rechnungen/Sonstige",
        "Newsletter",
        "Newsletter/Fitness",
        "Newsletter/Mode",
        "Newsletter/Business",
        "Newsletter/Shopping",
        "Newsletter/Coaching",
        "Newsletter/Kultur",
        "Newsletter/Versand",
        "Newsletter/Immobilien",
        "Newsletter/Reisen",
        "Newsletter/Unterhaltung",
        "Newsletter/Sonstige",
        "Social Media und Marketing",
        "Persoenlich",
        "Persoenlich/Julia Trost",
        "Persoenlich/Dan Rosen",
        "Persoenlich/Greator",
        "Persoenlich/Manychat",
        "Persoenlich/Alfima",
        "Persoenlich/Wispr Flow",
        "Behoerden",
        "Behoerden/WKO",
        "Behoerden/Steuerberater",
    ]
]

VERTICALKAY_FOLDERS = [
    imap_folder(f) for f in [
        "Studio",
        "Studio/Kursplanung",
        "Studio/Drop-in",
        "Kunden",
        "Kunden/Aktive",
        "Kunden/Anfragen",
        "Ausbildungen",
        "Ausbildungen/Anmeldungen",
        "Ausbildungen/Pruefungen",
        "Ausbildungen/Absolventen",
        "Events",
        "Events/JGA",
        "Events/Gruppenevents",
    ]
]

# ============================================================
# SORTIERREGELN — katarina@tolkmit.de
# ============================================================

# Absender → Rechnungsordner (exakter Absender-Match)
INVOICE_SENDER_MAP = {k: imap_folder(v) for k, v in {
    "paypal": "Rechnungen/PayPal",
    "apple": "Rechnungen/Apple",
    "itunes": "Rechnungen/Apple",
    "adobe": "Rechnungen/Adobe",
    "canva": "Rechnungen/Canva",
    "google": "Rechnungen/Google",
    "zoom": "Rechnungen/Zoom",
    "amazon": "Rechnungen/Amazon",
    "amazonpay": "Rechnungen/Amazon",
    "eversports": "Rechnungen/Eversports",
    "anthropic": "Rechnungen/Anthropic",
    "lagermax": "Rechnungen/Lagermax",
    "lagermax-edi": "Rechnungen/Lagermax",
    "americanexpress": "Rechnungen/Sonstige",
    "american express": "Rechnungen/Sonstige",
}.items()}

INVOICE_SUBJECT_KEYWORDS = [
    "rechnung", "invoice", "receipt", "quittung", "beleg",
    "zahlung bestätigt", "payment confirmation", "kaufbeleg",
    "transaktionsbeleg", "bestellbestätigung", "order confirmation",
    "ihre bestellung", "billing statement", "your receipt",
]

# Absender → Persönlich-Unterordner
PERSONAL_SENDER_MAP = {k: imap_folder(v) for k, v in {
    "julia trost": "Persoenlich/Julia Trost",
    "juliatrost": "Persoenlich/Julia Trost",
    "julia@": "Persoenlich/Julia Trost",
    "dan rosen": "Persoenlich/Dan Rosen",
    "danrosen": "Persoenlich/Dan Rosen",
    "dan@": "Persoenlich/Dan Rosen",
    "poledancewithdan": "Persoenlich/Dan Rosen",
    "danielrosen-pole": "Persoenlich/Dan Rosen",
    "lore@tolkmit.de": "Persoenlich/Julia Trost",
    "greator": "Persoenlich/Greator",
    "manychat": "Persoenlich/Manychat",
    "email.manychat.com": "Persoenlich/Manychat",
    "alfima.io": "Persoenlich/Alfima",
    "alfima.com": "Persoenlich/Alfima",
    "afm-media.com": "Persoenlich/Alfima",
    "mail.wispr.ai": "Persoenlich/Wispr",
    "wispr.ai": "Persoenlich/Wispr",
}.items()}

SOCIAL_MEDIA_SENDERS = [
    "instagram", "facebook", "tiktok", "youtube", "pinterest",
    "threads", "twitter", "x.com",
]

# Steuerberater: Judith Schimmerl (immer → Steuerberater)
STEUERBERATER_SENDERS = ["judithschimmerl@gmx.at"]

# WKO Absender-Domains
WKO_SENDERS = ["wko.at", "@wko.", "wkooe.at", "wirtschaftskammer", "fidw@", "frau in der wirtschaft", "frauinderwirtschaft", "epu@wko"]

# Behörden-Absender (direkt)
AUTHORITY_SENDERS = [
    "verbund.at", "info.verbund.at", "noreply@verbund", "salzburg-ag.at",
    "ooev.at", "vb-ooe.at", "volksbank", "bank99.at",
    "finanzamt", "sozialversicherung", "svs.at", "magistrat",
    "arbeiterkammer", "ak.at",
]

AUTHORITY_KEYWORDS = [
    "finanzamt", "sozialversicherung", "svs", "steuer", "behörde",
    "magistrat", "bescheid", "wirtschaftskammer", "wko", "gebühren",
    "gerichtskasse", "finanzpolizei", "arbeiterkammer", "ak ",
]

NEWSLETTER_INDICATORS = [
    "list-unsubscribe", "newsletter", "unsubscribe",
    "abmelden", "no-reply", "noreply", "donotreply",
    "marketing", "promotion", "offer", "angebot",
]

# Newsletter-Kategorisierung — Reihenfolge = Priorität
NEWSLETTER_CATEGORIES = [
    (imap_folder("Newsletter/Coaching"), [
        # bekannte Coaches/Absender zuerst (höchste Priorität)
        "judith hoffmann", "judithhoffmann", "judithhoffmann.info",
        "dirk kreuter", "dirkkreuter",
        "christian bischoff", "katja porsch", "caroline preuss", "carolinepreuss",
        "philipp kammerer", "philippkammerer", "birgit fortunati", "meetbirgit",
        "cedric mattig", "nice-publishing", "jens illgner", "roadtoglory",
        "maximilian raabe", "kicreatorakademie", "niels klement", "perspective.co",
        "timo maletschek", "maletschekcoaching", "shortwebinar",
        "christinasternbauer", "iris von the new you", "thenewyou",
        "torben platzer", "tpa-media", "susanne & nicole", "up-lift",
        "tanja kammler", "tanjakammler", "thebrandboutique",
        "bambusiness", "bam business", "mehr-geschaeft.com",
        "andreasbaulig", "bingo@patreon", "masterclass.com",
        "sigrun.com", "aufstehn.at", "als-coach-ausgebucht",
        "bold-brands.de", "sonneimkopf", "reneemoore", "katcoroy",
        "katrinhill", "freedom-writer", "expertenbuch", "affiliatesecrets",
        "mentortools", "thisismarketing", "vivian-dambeck", "goenuelpehlivan",
        "next-wave-consulting", "maximiliansaal", "fussbusiness",
        "schmitzemail.com", "easyrich-mind.com", "nataliesantarosa.com",
        "ericsteigner.de", "laurendallascreatorhub.com", "futurefemaleshq.co",
        "expertenportal.com", "ablefy.io", "digitalbeats.de",
        "certified-excellence.com", "thorben-seewig.de",
        "als-coach-ausgebucht.de", "mariolueddemann.com", "remotewoman.com",
        "hermannscherer.com", "marcelschlee.de", "nexteracoach.com",
        "brendon.com", "marinapersano.com", "schueder-consulting.de",
        "elevaty.de", "akquise.de", "social4success.de", "nextheroes.de",
        "shp-potential.com", "felix-stahl.de", "eberharter-consulting.at",
        "copycircle.de", "floriangehring.de", "dominikgoerke.de",
        "ads-atelier.com", "musesacademy.io", "matthewismith.com",
        "coachy.net", "ekatharinamacri.com", "her-closing-academy.de",
        "energie-ausbildung.com", "masters-of-marketing.de",
        "alex-fischer-duesseldorf.com", "ce-digital.de", "clublifedesign.com",
        "the-affiliate-code.de", "vermoegensbaum.de", "erfolgreichundfrei.com",
        "healing-humans.de", "healversity.com", "studiogrow.co", "passion-island.de",
        "lovelifepassport.com", "investmentpunk.academy", "thelifehacklibrary.com",
        "certified-excellence.com", "nataliesantarosa.com", "ericsteigner.de",
        "pathsocial", "path-social",
        "dirk wannmacher", "dirkwannmacher", "petralehner", "setup-dubai",
        "fortune-family", "katharina", "alfima",
        # Keywords
        "persönlichkeitsentwicklung", "mindset", "selbstentwicklung",
        "life coaching", "lifecoaching", "mentoring", "mentaltraining",
        "manifestation", "abundance", "erfolg", "selbstliebe",
    ]),
    (imap_folder("Newsletter/Fitness"), [
        # bekannte Pole/Fitness Absender
        "indipoledance", "indi pole", "flowmovement", "flow movement",
        "bodybyfrantraining", "body by fran", "engineered-life", "body engineers",
        "yogainternational", "yoga international", "yogaeasy",
        "hirefrederick", "body & pole", "body and pole",
        "charlottepolefit", "kiranoiredanceschool", "pdfamsterdam",
        "the-spin-off", "spin off", "lovelifepassport",
        "indigourlaub",
        # Keywords
        "pole", "aerial", "hoop", "dance", "stretching", "fitness",
        "yoga", "pilates", "sport", "workout", "movement",
        "wellness", "gesundheit", "health", "polerina", "polejunkie",
        "shining moments", "off the pole", "kineto", "organicfit",
        "pelvic", "longevity", "shapeshifter", "aloyoga", "alo ",
        "the-spin-off", "newsflash@the-spin-off", "pdaonline.com.au",
        "elizabethbfit", "gravityarts.ch", "aerialsilk",
        "bodybyfrantraining", "pilatesflows", "sisers-stretching",
        "kiranoiredanceschool", "pdfamsterdam", "hirefrederick",
        "thepolept", "polefreaks", "myorganicapps",
        "liebscher-bracht", "beck-balance", "teambasework",
        "medical-health-academy",
    ]),
    (imap_folder("Newsletter/Mode"), [
        # bekannte Marken/Absender
        "repetto", "moncler", "maje", "tezenis", "calzedonia",
        "falconeri", "kiko", "seidentraum", "guess", "laetitiachannel",
        "deutschesmodeinstitut", "fashion-procreate", "tanjakammler",
        "pavemodelmanagement", "iamfashionglobal", "dsoa.com",
        "patrizia pepe", "montclair", "montclare", "polwear",
        "fabrichouse", "fabric house", "corseterie",
        "radpolewear", "rad polewear", "polejunkie", "aloyoga", "alo yoga",
        "hellaheels", "hella heels", "clubhellaheels",
        "patriziapepe.com", "patrizia pepe",
        "polesportshop", "highonheelsonline", "high on heels",
        # Keywords
        "fashion", "mode", "style", "outfit", "kollektion", "collection",
        "kleid", "boutique", "luxus", "accessoire", "couture", "designer",
        "h&m", "zara", "kleidung", "dressing", "modell", "catwalk",
    ]),
    (imap_folder("Newsletter/Business"), [
        # bekannte Business-Absender
        "linkedin", "zapier", "later", "samcart", "teachable", "gumroad",
        "digistore24", "rankingcoach", "memberboost", "funnellab",
        "leadscripts", "patreon", "eventbrite", "calendly",
        "baulig", "andreasbaulig", "hoerhan", "pjmueller", "pjm investment",
        "shopify", "wix", "squarespace", "convertkit", "mailchimp",
        "virtuagym", "elementor", "perspective.co",
        "immobilienscout", "immoscout", "immowelt",
        "die-website-spezialisten", "kaiserweb.at", "pathsocial",
        "gyms1.com", "mindbodyonline", "wellhub", "egym-wellpass",
        "growthlayne", "webby.app", "neuroflash", "magicpen@neuroflash",
        # Keywords
        "investment", "business", "entrepreneur", "masterclass",
        "mehr geschaeft", "finanzen", "vermoegen", "immobilien",
        "unternehmen", "marketing", "seo", "social media strategie",
        "onlineexperten", "online experten",
    ]),
    (imap_folder("Newsletter/Kultur"), [
        # bekannte Absender
        "landestheater", "theater", "oper ", "museum",
        "salzburgfestival.at", "starlitefestival", "statisterie",
        "allevents.in",
        # Keywords
        "kultur", "freizeit", "entertainment", "veranstaltung",
        "lira.hu", "lira könyv", "bücher", "buch", "lesung",
        "konzert", "ausstellung", "kino", "veranstaltung",
        "voyage prive", "voyageprive", "lovelifepassport",
        # Keywords
        "kultur", "freizeit", "entertainment", "veranstaltung",
        "ticket", "eintrittskarte", "show", "event ",
    ]),
    (imap_folder("Newsletter/Unterhaltung"), [
        "primevideo.com", "channels.primevideo.com", "audible.de", "mail.audible.de",
        "paramountplus.com", "email.paramountplus.com", "transactions.paramountplus.com",
        "spotify.com", "netflix.com", "disneyplus.com", "joyn.at",
        "amazon music", "apple tv",
    ]),
    (imap_folder("Newsletter/Reisen"), [
        "trainline.com", "booking.com", "opodo.com", "contact.opodo.com", "easyjet.com",
        "driveme.co.at", "mohr-life-resort.at", "gruenauerhof.at", "mydays.at", "email.mydays.at",
        "buelow-hotels.de", "qualitando.email", "voyagepr",
        "hotel24.eu",
        "airbnb", "ryanair", "austrianairlines", "lufthansa", "wizzair",
        # Keywords
        "reise", "urlaub", "hotel", "flug", "buchungsbestaetigung", "reisebestaetigung",
    ]),
    (imap_folder("Newsletter/Immobilien"), [
        "immobilienscout24", "immowelt", "bamberger-immobilien", "immobilien-kurz",
        "k3-immo", "immo-", "@immo.", "immobilien", "liegenschaft",
    ]),
    (imap_folder("Newsletter/Versand"), [
        "gls-group", "gls.at", "gls.de", "ups.com", "fedex", "dhl.com", "dhl.de",
        "dpd.com", "dpd.at", "myhermes", "hermes.de", "post.at", "bpost",
        "sendungsverfolgung", "tracking", "paketankuendigung", "zustellbenachrichtigung",
        "deine sendung", "dein paket", "ihre sendung", "ihr paket",
    ]),
    (imap_folder("Newsletter/Shopping"), [
        # bekannte Shops
        "topcashback", "fleurop", "mymuesli", "weward",
        "vanicosmetics", "vani cosmetics", "lemalab", "sunday-natural",
        "tierliebhaber", "betreut.at", "vistaprint",
        "microsoft store", "microsoftstore",
        "ringana.com", "hellofresh.at", "hellofresh.de",
        "zaversky-shop.at", "evlis-needle.de", "marlenespetshop.com",
        "naturally-pam.de", "thebettercat.com", "drseverin.com",
        "email.everdrop.com", "info@everdrop.de", "everdrop.de",
        "monatglobal.com", "allevents.in",
        "lidl", "kaufland", "edeka", "rewe", "aldi", "dm-",
        "rossmann", "penny", "billa", "spar", "intersport", "decathlon",
        "zalando", "aboutyou", "otto", "amazon",
        "matsato", "soothrelieve", "lemalab",
        # Keywords
        "cashback", "deal", "rabatt", "sale", "discount",
        "gutschein", "outlet", "bestellung", "lieferung",
    ]),
]
NEWSLETTER_FALLBACK = imap_folder("Newsletter/Sonstige")

# ============================================================
# SORTIERREGELN — office@verticalkay.de
# ============================================================

# Bekannte Absender → direkter Ordner (verticalkay)
VERTICALKAY_SENDER_RULES = [
    (senders, imap_folder(f)) for senders, f in [
        # Wellpass / Gyms → Studio
        (["egym-wellpass.com", "wellhub.com", "email.wellhub.com", "gyms1.com", "mindbodyonline.com"], "Studio/Kursplanung"),
        # Ausbildungsanbieter → Ausbildungen
        (["individuell", "personalwomanakademie.com", "elizabethbfit", "gravityarts.ch",
          "hochseilgarten", "ausbildungsinstitut"], "Ausbildungen/Anmeldungen"),
    ]
]

VERTICALKAY_SUBJECT_RULES = [
    (kws, imap_folder(f)) for kws, f in [
        (["jga", "junggesell", "abschied", "hen night", "hen party"], "Events/JGA"),
        (["feier", "gruppe", "gruppenb", "event", "geburtstag", "party", "mädels"], "Events/Gruppenevents"),
        (["ausbildung", "trainer", "ausbilderin", "trainer-ausbildung", "zertifizierungskurs"], "Ausbildungen/Anmeldungen"),
        (["prüfung", "pruefung", "prüfungstermin", "zertifikat", "zertifizierung"], "Ausbildungen/Pruefungen"),
        (["absolvent", "bestanden", "glückwunsch", "abschluss"], "Ausbildungen/Absolventen"),
        (["buchung", "kurs", "termin", "stundenplan", "kursplan", "eversports", "wellpass", "check-in"], "Studio/Kursplanung"),
        (["warteliste", "drop-in", "dropin", "nachhol"], "Studio/Drop-in"),
        (["anfrage", "interesse", "anmeldung"], "Kunden/Anfragen"),
    ]
]

# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def decode_str(value):
    if not value:
        return ""
    try:
        parts = decode_header(value)
    except Exception:
        return str(value)
    result = ""
    for part, enc in parts:
        if isinstance(part, bytes):
            # "unknown-8bit" und andere defekte Encodings abfangen
            try:
                result += part.decode(enc or "utf-8", errors="replace")
            except (LookupError, TypeError):
                result += part.decode("latin-1", errors="replace")
        else:
            result += str(part)
    return result

def get_sender(msg):
    return decode_str(msg.get("From", "")).lower()

def get_subject(msg):
    return decode_str(msg.get("Subject", "")).lower()

def has_header(msg, header):
    return msg.get(header) is not None

def create_folder(mail, folder_name):
    """Ordner anlegen, wenn noch nicht vorhanden."""
    result = mail.create(folder_name)
    if result[0] == "OK":
        print(f"  ✓ Ordner erstellt: {folder_name}")
    # ALREADYEXISTS ist OK
    return True

def ensure_folders(mail, folders):
    """Alle Ordner anlegen (ignoriert bereits vorhandene)."""
    existing = []
    try:
        status, folder_list = mail.list()
        if status == "OK":
            for f in folder_list:
                if f:
                    existing.append(f.decode(errors="replace").lower())
    except Exception:
        pass

    for folder in folders:
        already = any(f'"{folder}"'.lower() in e or folder.lower() in e for e in existing)
        if not already:
            create_folder(mail, folder)
        else:
            print(f"  · Ordner vorhanden: {folder}")

def move_email(mail, uid, target_folder):
    """Mail per UID in Zielordner verschieben."""
    result = mail.uid("COPY", uid, target_folder)
    if result[0] == "OK":
        mail.uid("STORE", uid, "+FLAGS", "\\Deleted")
        return True
    return False

def classify_newsletter(sender, subject):
    """Newsletter einer der 5 Kategorien zuordnen."""
    combined = sender + " " + subject
    for folder, keywords in NEWSLETTER_CATEGORIES:
        for kw in keywords:
            if kw in combined:
                return folder
    return NEWSLETTER_FALLBACK

def sanitize_foldername(name):
    """Umlaute und Sonderzeichen für IMAP-Ordnernamen ersetzen."""
    replacements = {
        "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
        "Ä": "Ae", "Ö": "Oe", "Ü": "Ue",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "á": "a", "à": "a", "â": "a",
        "ó": "o", "ò": "o", "ô": "o",
        "ú": "u", "ù": "u", "û": "u",
        "ñ": "n", "ç": "c",
    }
    for char, replacement in replacements.items():
        name = name.replace(char, replacement)
    name = re.sub(r"[^\w\s\-]", "", name)
    return name.strip()

def extract_sender_name(from_field):
    """Lesbaren Absendernamen aus From-Header extrahieren."""
    from_field = decode_str(from_field)
    match = re.match(r'^"?([^"<]+)"?\s*<', from_field)
    if match:
        return sanitize_foldername(match.group(1).strip())
    match = re.match(r'([^@]+)@', from_field)
    if match:
        return sanitize_foldername(match.group(1).strip())
    return sanitize_foldername(from_field.split("@")[0].strip())

# ============================================================
# SORTIERLOGIK — tolkmit
# ============================================================

def classify_tolkmit(msg):
    sender = get_sender(msg)
    subject = get_subject(msg)

    # 1. Persönlich (VIP — höchste Priorität)
    for key, folder in PERSONAL_SENDER_MAP.items():
        if key in sender:
            return folder

    # 2. Steuerberater — Judith Schimmerl
    for addr in STEUERBERATER_SENDERS:
        if addr in sender:
            return imap_folder("Behoerden/Steuerberater")

    # 3. WKO
    for kw in WKO_SENDERS:
        if kw in sender:
            return imap_folder("Behoerden/WKO")

    # 4. Rechnungen — bekannte Absender
    for key, folder in INVOICE_SENDER_MAP.items():
        if key in sender:
            return folder

    # 5. Rechnungen — Betreff-Keywords
    for kw in INVOICE_SUBJECT_KEYWORDS:
        if kw in subject:
            return imap_folder("Rechnungen/Sonstige")

    # 6. Behörden & Verträge (direkte Absender + Keywords)
    for kw in AUTHORITY_SENDERS:
        if kw in sender:
            return imap_folder("Behoerden")
    for kw in AUTHORITY_KEYWORDS:
        if kw in sender or kw in subject:
            return imap_folder("Behoerden")

    # 7. Zugänge — NUR echte Kauf-Zugänge zu Lernplattformen
    ACCESS_SENDERS = [
        "digistore24", "thrivecart.net", "hotmart.com", "noreply@samcart",
        "mentortools.com", "wifi-ooe.at", "fortune-family", "coachy.net",
        "wondershare", "use.ai", "notification.use.ai",
        "learningsuite.io", "wordpress@queenwearofficial",
    ]
    ACCESS_SUBJECT_EXACT = [
        "bestellung erfolgreich / zugang", "kauf genehmigt! ihr zugang",
        "zugangsdaten für online-kurs", "deine zugangsdaten für",
        "your new password", "login details",
    ]
    sender_match = any(k in sender for k in ACCESS_SENDERS)
    subject_match = any(k in subject for k in ACCESS_SUBJECT_EXACT)
    if sender_match or subject_match:
        return "INBOX.Zugaenge"

    # 8. Social Media
    for kw in SOCIAL_MEDIA_SENDERS:
        if kw in sender:
            return imap_folder("Social Media und Marketing")

    # 8. Newsletter (List-Unsubscribe Header = sicheres Zeichen)
    if has_header(msg, "List-Unsubscribe"):
        return classify_newsletter(sender, subject)

    # 9. Newsletter-Indikatoren im Absender/Betreff
    for kw in NEWSLETTER_INDICATORS:
        if kw in sender or kw in subject:
            return classify_newsletter(sender, subject)

    return None  # Nicht klassifiziert → bleibt im INBOX

# ============================================================
# SORTIERLOGIK — verticalkay
# ============================================================

def classify_verticalkay(msg):
    sender = get_sender(msg)
    subject = get_subject(msg)
    combined = sender + " " + subject

    # Bekannte Absender zuerst
    for senders, folder in VERTICALKAY_SENDER_RULES:
        for s in senders:
            if s in sender:
                return folder

    for keywords, folder in VERTICALKAY_SUBJECT_RULES:
        for kw in keywords:
            if kw in combined:
                return folder

    # Eversports-Buchungen
    if "eversports" in sender:
        return "Studio/Kursplanung"

    # Allgemeine Anfragen → Neukunden
    if has_header(msg, "List-Unsubscribe") is False:
        return imap_folder("Kunden/Anfragen")

    return None

# ============================================================
# HAUPTFUNKTION
# ============================================================

def sort_mailbox(account_key, classify_fn, folders, sort_all=False):
    acc = ACCOUNTS[account_key]
    print(f"\n{'='*60}")
    print(f"Postfach: {acc['label']}")
    print(f"{'='*60}")

    try:
        mail = imaplib.IMAP4_SSL(acc["host"])
        mail.login(acc["username"], acc["password"])
        print("✓ Eingeloggt")
    except Exception as e:
        print(f"✗ Login fehlgeschlagen: {e}")
        return

    # Ordner anlegen
    print("\nOrdner prüfen / anlegen:")
    ensure_folders(mail, folders)

    # INBOX öffnen
    mail.select("INBOX")

    # Mails laden: alle oder nur ungelesene
    search_criteria = "ALL" if sort_all else "UNSEEN"
    status, data = mail.uid("SEARCH", "ALL" if sort_all else "UNSEEN")
    if status != "OK" or not data[0]:
        print(f"\nKeine Mails zum Sortieren.")
        mail.logout()
        return

    uids = data[0].split()
    print(f"\n{len(uids)} Mails zum Sortieren")

    moved = 0
    skipped = 0
    failed = 0

    for uid in uids:
        try:
            status, msg_data = mail.uid("FETCH", uid, "(RFC822)")
            if status != "OK" or not msg_data or not msg_data[0]:
                continue
            raw = msg_data[0][1]
            if not isinstance(raw, bytes):
                continue
            msg = email.message_from_bytes(raw, policy=email.policy.compat32)

            target = classify_fn(msg)

            if target:
                success = move_email(mail, uid, target)
                if success:
                    moved += 1
                else:
                    failed += 1
            else:
                skipped += 1

        except Exception as e:
            failed += 1
            continue

    mail.expunge()
    print(f"\n✓ Verschoben: {moved} | Unverändert (kein Match): {skipped} | Fehler: {failed}")
    mail.logout()


def main(sort_all=False):
    print("E-Mail Sortierer — Katarina Tolkmit")
    print(f"Modus: {'ALLE Mails' if sort_all else 'Nur neue Mails'}")

    sort_mailbox("tolkmit", classify_tolkmit, TOLKMIT_FOLDERS, sort_all=sort_all)
    sort_mailbox("verticalkay", classify_verticalkay, VERTICALKAY_FOLDERS, sort_all=sort_all)

    print("\n✅ Fertig.")


if __name__ == "__main__":
    import sys
    sort_all = "--all" in sys.argv
    main(sort_all=sort_all)
