import smtplib
from email.message import EmailMessage

def send_email(ad, env):
    """
    Sendet eine E-Mail-Benachrichtigung mit allen relevanten Informationen zur Anzeige.
    Die SMTP-Zugangsdaten und Empfänger werden aus dem env-Dictionary geladen.
    """
    msg = EmailMessage()
    msg["Subject"] = f"Neues Angebot: {ad['title']}"
    msg["From"] = env["EMAIL_USER"]
    msg["To"] = env["EMAIL_TO"]

    # Nachrichtentext mit allen Details zur Anzeige
    body = (
        f"Titel: {ad['title']}\n"
        f"Zustand: {ad['condition']}\n"
        f"Preis: {ad['price']} €\n"
        f"Versand: {ad['shipping']} €\n"
        f"Gesamt: {ad['total_price']} €\n"
        f"Entfernung: {ad['distance_km']} km\n"
        f"Ort: {ad['location']}\n"
        f"URL: {ad['url']}\n"
        f"Datum: {ad['date']}\n"
    )
    msg.set_content(body)

    # Sende die E-Mail über den konfigurierten SMTP-Server
    with smtplib.SMTP(env["EMAIL_HOST"], env["EMAIL_PORT"]) as server:
        server.starttls()  # Verschlüsselung aktivieren
        server.login(env["EMAIL_USER"], env["EMAIL_PASSWORD"])
        server.send_message(msg)
