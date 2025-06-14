# Kleinanzeigen Retro-Konsolen-Bot

Dieses Projekt durchsucht automatisch eBay Kleinanzeigen nach günstigen Retro-Konsolen, bewertet Zustand und Preis nach deinen Vorgaben und sendet dir eine Benachrichtigung per E-Mail, wenn ein interessantes Angebot gefunden wurde.

## Features

- Sucht nach vielen Retro-Konsolen (stationär und Handheld)
- Berücksichtigt Entfernung, Versandkosten und individuelle Preisgrenzen
- Erkennt defekte Geräte anhand von Keywords
- Nur neue und interessante Anzeigen werden gemeldet
- Benachrichtigung per E-Mail (SMTP)
- Speichert bereits bekannte Anzeigen in SQLite
- Konfiguration über `.env` und `console_rules.jsonc`
- Modularer Aufbau (Scraper, Analyzer, Notifier, Datenbank)

## Installation

```bash
pip install -r requirements.txt