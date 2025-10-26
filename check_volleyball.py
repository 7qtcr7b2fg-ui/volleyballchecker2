import requests
from bs4 import BeautifulSoup

URL = "https://cloud.aktivkonzepte.de/hspulm/kurse.html##/Home/Kurs/683"

def kurs_frei():
    # Header für realistischen Request (manche Seiten blocken "Bot"-Anfragen)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Seite abrufen
    r = requests.get(URL, headers=headers)
    if r.status_code != 200:
        print(f"⚠️ Fehler beim Abruf: {r.status_code}")
        return False

    # HTML analysieren
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text().lower()

    # Prüfen, ob „ausgebucht“ oder „belegt“ vorkommt
    if "ausgebucht" in text or "belegt" in text:
        return False
    else:
        return True

if __name__ == "__main__":
    if kurs_frei():
        print("✅ Volleyballkurs ist frei!")
        exit(0)
    else:
        print("❌ Kein Platz frei.")
        exit(1)
