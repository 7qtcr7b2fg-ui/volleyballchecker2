import requests
from bs4 import BeautifulSoup

URL = "https://campus.uni-ulm.de/qisserver/rds?state=wsearchv&search=1&veranstaltung.veranstid=12345"  # <-- hier deine Kurs-URL

def kurs_frei():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text().lower()
    # Wenn "keine plätze frei" NICHT vorkommt, ist der Kurs frei
    return "keine plätze frei" not in text and "belegt" not in text

if __name__ == "__main__":
    if kurs_frei():
        print("✅ Volleyballkurs ist frei!")
        exit(0)
    else:
        print("❌ Kein Platz frei.")
        exit(1)
