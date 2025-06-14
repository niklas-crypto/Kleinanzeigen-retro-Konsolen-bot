import sqlite3

DB_NAME = "ads.db"  # Name der SQLite-Datenbank

def init_db():
    """
    Erstellt die Tabelle 'ads', falls sie noch nicht existiert.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS ads (
            id TEXT PRIMARY KEY,
            title TEXT,
            url TEXT,
            price REAL,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def is_known_ad(ad_id):
    """
    Prüft, ob eine Anzeige bereits in der Datenbank gespeichert ist.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id FROM ads WHERE id=?", (ad_id,))
    result = c.fetchone()
    conn.close()
    return result is not None

def add_ad(ad):
    """
    Fügt eine neue Anzeige zur Datenbank hinzu (oder ignoriert sie, falls schon vorhanden).
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO ads (id, title, url, price, date) VALUES (?, ?, ?, ?, ?)",
              (ad['id'], ad['title'], ad['url'], ad['price'], ad['date']))
    conn.commit()
    conn.close()