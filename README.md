# 🚀 Omni-Messenger Marketing Automation System

A sophisticated marketing automation tool designed to manage and execute mass messaging across multiple platforms (**Telegram**, **Viber**, and **WhatsApp**) via a unified Telegram Bot interface. This was my first commercial freelance project, focusing on complex web and mobile automation.

---

### 🛠 Tech Stack
* **Language:** Python 3.x
* **Framework:** pyTelegramBotAPI (Telebot)
* **Automation:** * **Selenium WebDriver** (Web automation for Telegram & WhatsApp)
    * **Appium** (Mobile UI automation for Viber/Android)
* **Infrastructure:** * `localStorage` injection for session persistence
    * **Appium UiAutomator2** for Android interaction
    * **python-dotenv** for secure credential management
    * **fake-useragent** for anti-detection

---

### 🌟 Key Features

* **Multi-Platform Integration:** Automated messaging flows for **Telegram**, **Viber**, and **WhatsApp** from a single dashboard.
* **Advanced Authentication:** * **Telegram:** Injects `localStorage` data to bypass repeated QR/SMS logins.
    * **Viber:** Full Android emulation cycle, handling system permissions and OTP inputs via Appium.
    * **WhatsApp:** Web-based automation with specialized "Link with Phone Number" support.
* **Database Operations:** Built-in CRUD system to manage, search, and delete mailing templates directly through bot commands.
* **Anti-Bot Protection:** Implements human-like behavior using `random_sleep` intervals and simulated character-by-character typing.

---

### 🏗 Project Architecture
The system is modular, ensuring that platform-specific logic is isolated:
* `telegram_handler.py` — Manages Web-interface sessions and message delivery.
* `viber_handler.py` — Controls Android UI elements and app navigation.
* `whatsapp_handler.py` — Handles WhatsApp Web business logic and selectors.

---

### 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/myfish-code/Word-Learning-Tg-Bot](https://github.com/myfish-code/Telegram-Bot---Mailing)
   cd Word-Learning-Tg-Bot

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
  
3. **Environment Setup:**
   Create a `.env` file in the root directory and paste this:

   ```bash
   BOT_TOKEN=your_tg_token

4. **Run the bot:**
   ```
    Ensure Appium Server is running.
    Ensure ChromeDriver is installed.
  ```bash
   python main.py
