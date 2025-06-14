import requests
from bs4 import BeautifulSoup
import re

# Liste aller relevanten Konsolen-Suchbegriffe (Kleinanzeigen-Keywords)
KEYWORDS = [
    "ps2", "xbox", "gamecube", "psp", "2ds", "3ds", "3ds xl", "new 2ds xl", "new 3ds", "new 3ds xl",
    "wii", "wii u", "ps3", "ps1", "saturn", "dreamcast", "sega cd", "ps vita", "ds", "ds lite",
    "dsi", "dsi xl", "n64", "gameboy", "gameboy color", "gameboy advance", "gameboy advance sp",
    "genesis", "xbox 360", "snes", "nes"
]

# Basis-URL für Konsolen-Angebote auf Kleinanzeigen
BASE_URL = "https://www.kleinanzeigen.de/s-spielekonsole/c173"

def search_ads():
    """
    Sucht für jedes Keyword nach aktuellen Anzeigen auf eBay Kleinanzeigen.
    Gibt eine Liste von Anzeigen-Dictionaries zurück.
    """
    ads = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for keyword in KEYWORDS:
        params = {"keywords": keyword}
        try:
            res = requests.get(BASE_URL, params=params, headers=headers, timeout=15)
        except Exception as e:
            print(f"Fehler bei Anfrage für {keyword}: {e}")
            continue
        soup = BeautifulSoup(res.text, "html.parser")
        # Jede Anzeige entspricht einem <article class="aditem">-Element
        for item in soup.find_all("article", {"class": "aditem"}):
            ad_id = item.get("data-adid")
            title_tag = item.find("a", {"class": "ellipsis"})
            title = title_tag.get_text(strip=True) if title_tag else ""
            url = "https://www.kleinanzeigen.de" + title_tag["href"] if title_tag else ""
            price_tag = item.find("p", {"class": "aditem-main--middle--price-shipping--price"})
            price_text = price_tag.get_text(strip=True) if price_tag else ""
            price = float(re.sub(r"[^\d]", "", price_text)) if price_text else 0.0
            location_tag = item.find("div", {"class": "aditem-main--top--left"})
            location = location_tag.get_text(strip=True) if location_tag else ""
            date_tag = item.find("div", {"class": "aditem-main--top--right"})
            date = date_tag.get_text(strip=True) if date_tag else ""
            ads.append({
                "id": ad_id,
                "title": title,
                "url": url,
                "price": price,
                "location": location,
                "date": date,
                "keyword": keyword
            })
    return ads