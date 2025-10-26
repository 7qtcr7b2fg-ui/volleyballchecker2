import requests
from bs4 import BeautifulSoup

URL = "https://cloud.aktivkonzepte.de/hspulm/kurse.html#/Home/Kurs/683"

def kurs_frei():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    print(f"Status Code: {r.status_code}")

    if r.status_code != 200:
        print("❌ Fehler beim Abrufen der Seite.")
        return False

    # HTML speichern, um später nachzusehen
    with open("debug_output.html", "w", encoding="utf-8") as f:
        f.write(r.text)

    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text().lower()

    # Prüfen, ob der Kursname auftaucht
    if "volleyball techniktraining" in text:
        print("🏐 Kurs 'Volleyball Techniktraining' gefunden.")

        # Nun prüfen, ob dort 'ausgebucht' steht
        if "ausgebucht" in text:
            print("❌ Der Kurs ist AUSGEBUCHT.")
            return False
        else:
            print("✅ Der Kurs ist FREI!")
            return True
    else:
        print("⚠️ Kein Kurs namens 'Volleyball Techniktraining' gefunden.")
        return False

if __name__ == "__main__":
    kurs_frei()
