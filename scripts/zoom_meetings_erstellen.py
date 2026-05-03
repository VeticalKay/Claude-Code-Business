import requests
import base64
from datetime import datetime, timedelta

# Zoom API Zugangsdaten
ACCOUNT_ID = "GNuYhjlNT1KMfmTW7N8h8g"
CLIENT_ID = "kurLAXKxTkGTwmP2Ij8JQ"
CLIENT_SECRET = "tM04xt7Ie12t8BAVtKBNKYt5GF7DAaEb"

# Meetings konfigurieren
MEETINGS = [
    {"name": "Mai-Classes",       "start": "2026-05-01", "end": "2026-05-31"},
    {"name": "Juni-Classes",      "start": "2026-06-01", "end": "2026-06-30"},
    {"name": "Juli-Classes",      "start": "2026-07-01", "end": "2026-07-31"},
    {"name": "August-Classes",    "start": "2026-08-01", "end": "2026-08-31"},
    {"name": "September-Classes", "start": "2026-09-01", "end": "2026-09-30"},
    {"name": "Oktober-Classes",   "start": "2026-10-01", "end": "2026-10-31"},
    {"name": "November-Classes",  "start": "2026-11-01", "end": "2026-11-30"},
    {"name": "Dezember-Classes",  "start": "2026-12-01", "end": "2026-12-20"},
]


def get_token():
    url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={ACCOUNT_ID}"
    credentials = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {"Authorization": f"Basic {credentials}"}
    r = requests.post(url, headers=headers)
    r.raise_for_status()
    return r.json()["access_token"]


def first_weekday(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    while d.weekday() >= 5:  # Samstag=5, Sonntag=6
        d += timedelta(days=1)
    # Sommerzeit (CEST) April–Oktober = UTC+2, Winterzeit (CET) Nov–März = UTC+1
    offset = "+02:00" if 4 <= d.month <= 10 else "+01:00"
    return d.strftime("%Y-%m-%dT15:00:00") + offset


def create_meeting(token, meeting):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = {
        "topic": meeting["name"],
        "type": 8,  # Wiederkehrend mit fixer Zeit
        "start_time": first_weekday(meeting["start"]),
        "duration": 360,  # 6 Stunden (15:00–21:00)
        "timezone": "Europe/Vienna",
        "recurrence": {
            "type": 2,           # Wöchentlich
            "repeat_interval": 1,
            "weekly_days": "2,3,4,5,6",  # Mo–Fr
            "end_date_time": meeting["end"] + "T23:59:59Z",
        },
        "settings": {
            "join_before_host": True,
            "waiting_room": False,
            "host_video": True,
            "participant_video": True,
        },
    }
    r = requests.post("https://api.zoom.us/v2/users/me/meetings", headers=headers, json=body)
    return r.json()


def main():
    print("Hole Zoom Token...\n")
    token = get_token()
    print("Token OK\n")

    results = []
    for m in MEETINGS:
        result = create_meeting(token, m)
        if "join_url" in result:
            print(f"{m['name']:25} {result['join_url']}")
            results.append(f"{m['name']}: {result['join_url']}")
        else:
            print(f"{m['name']:25} FEHLER: {result.get('message', result)}")

    # Ergebnisse speichern
    with open("zoom_links.txt", "w") as f:
        f.write("\n".join(results))
    print("\nLinks gespeichert in: zoom_links.txt")


if __name__ == "__main__":
    main()
