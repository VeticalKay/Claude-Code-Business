#!/usr/bin/env python3
"""
Buchhaltungs-Automatisierung — Katarina Tolkmit
Sortiert Eingangs- (ER) und Ausgangsrechnungen (AR) automatisch in iCloud Drive.
Läuft täglich automatisch via cron job.
"""

import imaplib
import email
import os
import re
import json
from datetime import datetime
from pathlib import Path
from email.header import decode_header
from email.utils import parsedate_to_datetime

# ============================================================
# KONFIGURATION — Passwörter hier eintragen
# ============================================================

ACCOUNTS = [
    {
        "name": "Tolkmit",
        "host": "imap.tng.de",
        "username": "ktolkmit",
        "password": "HIER_TOLKMIT_PASSWORT",
        "sent_folder": "Gesendet",
    },
    {
        "name": "Verticalkay",
        "host": "server1.codeking.at",
        "username": "office@verticalkay.de",
        "password": "HIER_VERTICALKAY_PASSWORT",
        "sent_folder": "Sent Messages",
    },
    {
        "name": "iCloud",
        "host": "imap.mail.me.com",
        "username": "kayto_design@icloud.com",
        "password": "HIER_ICLOUD_APP_PASSWORT",  # App-spezifisches Passwort!
    },
]

# ============================================================
# ORDNERSTRUKTUR
# iCloud Drive/Dokumente/Katarina 2026/Steuererklärung/ER/Mai/
# ============================================================

ICLOUD_BASE = os.path.expanduser(
    "~/Library/Mobile Documents/com~apple~CloudDocs/Dokumente"
)

MONTHS_DE = {
    1: "Januar", 2: "Februar", 3: "März", 4: "April",
    5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
    9: "September", 10: "Oktober", 11: "November", 12: "Dezember"
}

# Suchbegriffe für Rechnungserkennung
INVOICE_KEYWORDS = [
    "rechnung", "invoice", "receipt", "quittung", "beleg",
    "zahlung bestätigt", "order confirmation", "your order",
    "faktura", "billing", "payment confirmation", "kaufbeleg",
    "transaktionsbeleg", "ihre bestellung", "bestellbestätigung"
]

# Bekannte Anbieter → saubere Namen
KNOWN_SENDERS = {
    "paypal": "PayPal",
    "canva": "Canva",
    "eversports": "Eversports",
    "google": "Google",
    "apple": "Apple",
    "zoom": "Zoom",
    "adobe": "Adobe",
    "amazon": "Amazon",
    "greator": "Greator",
    "julia trost": "JuliaTrost",
    "juliatrost": "JuliaTrost",
    "verticalo": "Verticalo",
}

# Protokoll bereits verarbeiteter E-Mails (verhindert Duplikate)
PROCESSED_FILE = os.path.expanduser("~/.buchhaltung_processed.json")

# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def load_processed():
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_processed(processed):
    with open(PROCESSED_FILE, "w") as f:
        json.dump(list(processed), f)

def decode_str(s):
    if not s:
        return ""
    parts = decode_header(s)
    result = ""
    for part, enc in parts:
        if isinstance(part, bytes):
            result += part.decode(enc or "utf-8", errors="replace")
        else:
            result += str(part)
    return result

def is_invoice(subject, sender):
    text = (subject + " " + sender).lower()
    return any(kw in text for kw in INVOICE_KEYWORDS)

def extract_invoice_number(subject, body=""):
    patterns = [
        r'(?:rg|re|inv|nr|no|#)[.\-\s]*([A-Z0-9\-]{4,20})',
        r'([A-Z]{2,4}-\d{4,10})',
        r'(\d{6,12})',
    ]
    for pattern in patterns:
        m = re.search(pattern, subject + " " + body, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return "unbekannt"

def clean_name(sender):
    name = re.sub(r'<.*?>', '', sender).strip().strip('"')
    if not name:
        m = re.search(r'([^@]+)@', sender)
        name = m.group(1) if m else sender

    name_lower = name.lower()
    for key, clean in KNOWN_SENDERS.items():
        if key in name_lower:
            return clean

    name = re.sub(r'[^\w\s]', '', name).strip().replace(' ', '')[:20]
    return name or "Unbekannt"

def get_folder(date, doc_type):
    year = date.strftime("%Y")
    month = MONTHS_DE[date.month]
    path = Path(ICLOUD_BASE) / f"Katarina {year}" / "Steuererklärung" / doc_type / month
    path.mkdir(parents=True, exist_ok=True)
    return path

def build_filename(date, doc_type, name, inv_num):
    d = date.strftime("%Y-%m-%d")
    n = re.sub(r'[^\w\-]', '', name)[:20]
    i = re.sub(r'[^\w\-]', '', inv_num)[:15]
    return f"{d}_{doc_type}_{n}_{i}.pdf"

# ============================================================
# HAUPTLOGIK
# ============================================================

def process_folder(account, imap, folder, doc_type, processed):
    count = 0
    try:
        status, _ = imap.select(f'"{folder}"')
        if status != 'OK':
            status, _ = imap.select(folder)
        if status != 'OK':
            print(f"    ⚠ Ordner '{folder}' nicht gefunden")
            return 0
    except Exception as e:
        print(f"    ⚠ {e}")
        return 0

    _, msg_ids = imap.search(None, 'SINCE', '01-Jan-2025')
    if not msg_ids[0]:
        return 0

    for msg_id in msg_ids[0].split():
        uid = f"{account['name']}_{folder}_{msg_id.decode()}"
        if uid in processed:
            continue

        try:
            _, data = imap.fetch(msg_id, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])

            subject = decode_str(msg.get('Subject', ''))
            sender = decode_str(msg.get('From', ''))

            if not is_invoice(subject, sender):
                processed.add(uid)
                continue

            # Datum
            try:
                date = parsedate_to_datetime(msg.get('Date', ''))
            except Exception:
                date = datetime.now()

            # PDF-Anhänge
            for part in msg.walk():
                ct = part.get_content_type()
                fn = part.get_filename()
                is_pdf = ct == 'application/pdf' or (fn and fn.lower().endswith('.pdf'))
                if not is_pdf:
                    continue

                pdf_data = part.get_payload(decode=True)
                if not pdf_data:
                    continue

                name = clean_name(sender)
                inv_num = extract_invoice_number(subject)
                folder_path = get_folder(date, doc_type)
                filename = build_filename(date, doc_type, name, inv_num)
                filepath = folder_path / filename

                # Duplikat vermeiden
                c = 1
                while filepath.exists():
                    filepath = folder_path / build_filename(date, doc_type, name, f"{inv_num}_{c}")
                    c += 1

                filepath.write_bytes(pdf_data)
                print(f"    ✓ {filename}")
                count += 1

            processed.add(uid)

        except Exception as e:
            print(f"    ✗ Fehler bei Nachricht {msg_id}: {e}")

    return count

def run():
    processed = load_processed()
    total = 0

    print(f"\n🗂  Buchhaltung — {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("=" * 50)

    for account in ACCOUNTS:
        print(f"\n📬 {account['name']}")
        try:
            imap = imaplib.IMAP4_SSL(account['host'])
            imap.login(account['username'], account['password'])

            # Eingangsrechnungen
            print("  ER (Eingang):")
            n = process_folder(account, imap, 'INBOX', 'ER', processed)
            total += n
            if n == 0:
                print("    — keine neuen")

            # Ausgangsrechnungen
            sent = account.get('sent_folder', 'Sent Messages')
            print("  AR (Gesendet):")
            n = process_folder(account, imap, sent, 'AR', processed)
            total += n
            if n == 0:
                print("    — keine neuen")

            imap.logout()

        except Exception as e:
            print(f"  ✗ Verbindungsfehler: {e}")

    save_processed(processed)
    print(f"\n✅ {total} neue Datei(en) gespeichert")
    print("=" * 50)

if __name__ == "__main__":
    run()
