import requests
from bs4 import BeautifulSoup

URL = "https://cloud.aktivkonzepte.de/hspulm/kurse.html##/Home/Kurs/683"

def kurs_frei():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    print(f"Status Code: {r.status_code}")

    # gesamten Text speichern, um zu prüfen, was tatsächlich geladen wird
    with open("debug_output.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("✅ HTML-Inhalt wurde in debug_output.html gespeichert")

    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text().lower()

    print("\n--- AUSZUG AUS TEXT ---")
    print(text[:1000])  # erste 1000 Zeichen zur Kontrolle
    print("------------------------\n")

    if "ausgebucht" in text or "belegt" in text:
        print("❌ 'ausgebucht' oder 'belegt' gefunden!")
        return False
    else:
        print("✅ Kein 'ausgebucht' gefunden!")
        return True

if __name__ == "__main__":
    kurs_frei()
