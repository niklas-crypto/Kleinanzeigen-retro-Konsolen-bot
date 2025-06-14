import time
from utils import load_env, load_console_rules
from db import init_db, is_known_ad, add_ad
from scraper import search_ads
from analyzer import analyze_ad
from notifier import send_email

def main():
    # Lade Konfiguration (.env) und Preisregeln (console_rules.jsonc)
    env = load_env()
    rules = load_console_rules()
    # Initialisiere Datenbank (legt sie ggf. an)
    init_db()
    print("Starte Retro-Konsolen-Bot...")

    # Endlosschleife: Suche regelmäßig nach neuen Anzeigen
    while True:
        print("Suche nach neuen Anzeigen...")
        ads = search_ads()
        for ad in ads:
            # Prüfe, ob Anzeige schon bekannt (bereits gemeldet oder verarbeitet)
            if not is_known_ad(ad["id"]):
                # Bewertet Anzeige nach Preis, Zustand und Versand
                analyzed = analyze_ad(ad, rules, env["HOME_ADDRESS"])
                if analyzed:
                    # Sende E-Mail, wenn Anzeige interessant ist
                    send_email(analyzed, env)
                    print(f"Benachrichtigung für {ad['title']} gesendet.")
                # Anzeige merken, damit sie nicht nochmal gemeldet wird
                add_ad(ad)
        print(f"Warte {env['CHECK_INTERVAL_MINUTES']} Minuten...")
        time.sleep(env["CHECK_INTERVAL_MINUTES"] * 60)

if __name__ == "__main__":
    main()