from playwright.sync_api import sync_playwright
import time

URL = "https://cloud.aktivkonzepte.de/hspulm/kurse.html#/Home/Kurs/683"

def kurs_frei():
    print("🚀 Starte Headless-Browser...")
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        print("🌐 Lade Seite...")
        page.goto(URL, wait_until="networkidle")

        # kurz warten, damit die Seite ihren JS-Inhalt lädt
        time.sleep(5)

        content = page.content().lower()

        # Debug speichern
        with open("debug_rendered.html", "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()

        if "volleyball techniktraining" in content:
            print("🏐 Kurs 'Volleyball Techniktraining' gefunden!")

            if "ausgebucht" in content:
                print("❌ Kurs ist AUSGEBUCHT.")
                return False
            else:
                print("✅ Kurs ist FREI!")
                return True
        else:
            print("⚠️ Kein Volleyballkurs gefunden.")
            return False

if __name__ == "__main__":
    kurs_frei()
