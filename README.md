
## 🚀 Installation & Setup Guide

### Prerequisites

- **Python 3.8 or higher**  
  [Download Python here](https://www.python.org/downloads/)
- **Git**  
  [Download Git here](https://git-scm.com/downloads)
- A valid **SMTP email account** for notifications (e.g., Gmail, GMX, Outlook, etc.)

---

### 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/niklas-crypto/Kleinanzeigen-retro-Konsolen-bot.git
cd Kleinanzeigen-retro-Konsolen-bot
```

---

### 2. (Recommended) Create and Activate a Virtual Environment

This keeps your dependencies isolated from other projects.

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root folder.  
Copy and edit the example below with your own information:

```env
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_USER=your.email@example.com
EMAIL_PASSWORD=yourEmailPassword
EMAIL_TO=your.email@example.com
HOME_ADDRESS=Your Street 1, 12345 YourCity
CHECK_INTERVAL_MINUTES=30
```

**Field explanations:**

- `EMAIL_HOST`, `EMAIL_PORT` — SMTP settings for your email provider
- `EMAIL_USER`, `EMAIL_PASSWORD` — Your email login credentials
- `EMAIL_TO` — The recipient address for notifications (typically your own)
- `HOME_ADDRESS` — Your home address (used for distance calculation)
- `CHECK_INTERVAL_MINUTES` — How often to check for new ads (in minutes)

---

### 5. Review and Adjust Console Price Rules

The file `console_rules.jsonc` defines the maximum price you want to pay for each console, both working and defective.  
Feel free to edit this file to fit your budget and preferences.

> **Note:** The `.jsonc` extension allows comments for your convenience.  
> If you remove all comments, you can rename it to `.json`.

---

### 6. Run the Bot

Start the bot with:

```bash
python main.py
```

The bot will search for new ads at your chosen interval and notify you via email if any matching offers are found.

---

### Additional Notes

- The bot stores seen ads in an `ads.db` SQLite database file (created automatically).
- The HTML structure of Kleinanzeigen may change, which could require updates to the scraper.
- The notification system uses your SMTP credentials—never share your `.env` file!
- For troubleshooting, review error messages in your terminal.

---

**Happy collecting! 🎮**  
If you have any questions or need help, feel free to open an issue on [GitHub](https://github.com/niklas-crypto/Kleinanzeigen-retro-Konsolen-bot/issues).
```

**Füge diesen gesamten Codeblock in dein `README.md` ein – damit ist der gesamte Installationsprozess ausführlich und übersichtlich dokumentiert!**