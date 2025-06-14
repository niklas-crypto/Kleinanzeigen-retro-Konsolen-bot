import re
from utils import calc_distance_km, is_bielefeld

# Schlüsselwörter, um defekte oder funktionierende Geräte zu erkennen
DEFECTIVE_WORDS = ["defekt", "kaputt", "ohne funktion", "nicht funktion", "als ersatzteil"]
WORKING_WORDS = ["funktioniert", "getestet", "läuft", "funktionsfähig", "funktionstüchtig"]

def analyze_ad(ad, rules, home_address):
    """
    Bewertet eine Anzeige hinsichtlich Zustand, Versand, Preis und Preislimit.
    Gibt das Anzeige-Objekt mit Zusatzinfos zurück, falls es den Preisregeln entspricht, sonst None.
    """
    # Text aus Titel und (sofern vorhanden) Beschreibung durchsuchen
    title_text = (ad['title'] + " " + ad.get('desc', "")).lower()
    # Prüfen, ob das Gerät als defekt oder funktionierend markiert ist
    is_defective = any(word in title_text for word in DEFECTIVE_WORDS)
    is_working = any(word in title_text for word in WORKING_WORDS) and not is_defective

    # Entfernung zum Heimatstandort berechnen
    dist = calc_distance_km(home_address, ad["location"])
    shipping = 0
    # Versandkostenpauschale, falls weiter als 25km entfernt (außer Bielefeld)
    if dist > 25 and not is_bielefeld(ad["location"]):
        shipping = 7.69

    # Hole Preisregel für diese Konsole
    key = ad["keyword"].lower()
    rule = rules.get(key)
    if not rule:
        return None  # Keine Regel gefunden, Anzeige ignorieren

    # Preisgrenze je nach Zustand bestimmen
    max_price = rule["max_price_defective"] if is_defective else rule["max_price_working"]
    total_price = ad["price"] + shipping

    # Wenn Gesamtpreis unter der Grenze, Anzeige zurückgeben, sonst ignorieren
    if total_price <= max_price:
        ad.update({
            "condition": "defekt" if is_defective else "funktionierend",
            "distance_km": round(dist, 1),
            "shipping": shipping,
            "total_price": total_price
        })
        return ad
    return None