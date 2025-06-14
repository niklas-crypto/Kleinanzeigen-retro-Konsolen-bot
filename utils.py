import os
import json
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Lädt Umgebungsvariablen aus der .env-Datei
load_dotenv()

def load_env():
    """Lädt Konfiguration aus der .env-Datei in ein Dictionary."""
    return {
        "EMAIL_HOST": os.getenv("EMAIL_HOST"),
        "EMAIL_PORT": int(os.getenv("EMAIL_PORT")),
        "EMAIL_USER": os.getenv("EMAIL_USER"),
        "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD"),
        "EMAIL_TO": os.getenv("EMAIL_TO"),
        "HOME_ADDRESS": os.getenv("HOME_ADDRESS"),
        "CHECK_INTERVAL_MINUTES": int(os.getenv("CHECK_INTERVAL_MINUTES"))
    }

def load_console_rules(path="console_rules.jsonc"):
    """Lädt Konsolen-Preisregeln aus JSON-Datei. Entfernt Kommentare für JSONC."""
    with open(path, encoding="utf-8") as f:
        # Entfernt Zeilen, die mit // beginnen
        lines = [line for line in f if not line.strip().startswith("//")]
        content = "".join(lines)
        return json.loads(content)

def get_lat_lon(address):
    """Gibt (Breite, Länge) für eine Adresse zurück."""
    geolocator = Nominatim(user_agent="retro_bot")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    raise ValueError(f"Adresse nicht gefunden: {address}")

def calc_distance_km(addr1, addr2):
    """Berechnet die Luftlinien-Entfernung in km zwischen zwei Adressen."""
    latlon1 = get_lat_lon(addr1)
    latlon2 = get_lat_lon(addr2)
    return geodesic(latlon1, latlon2).km

def is_bielefeld(address):
    """Prüft, ob die Adresse zu Bielefeld gehört (für Versandregel)."""
    return "bielefeld" in address.lower()