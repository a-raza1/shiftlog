---

```markdown
# ShiftLog Pro 🕒

ShiftLog Pro is a secure, lightweight web application built with Flask and SQLAlchemy. It is specifically designed to provide a native-feeling iOS experience for tracking work hours, managing employers, and calculating weekly/monthly totals.



---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Windows Installation](#windows-installation)
3. [macOS Installation](#macos-installation)
4. [Linux Installation](#linux-installation)
5. [Application Structure](#application-structure)
6. [Security & Customization](#security--customization)

---

## 🛠 Prerequisites

Regardless of your OS, you must have the following installed:
- **Python 3.10+** (Ensure "Add to PATH" is checked on Windows)
- **Pip** (Python Package Manager)
- **A Local Network** (To connect your iPhone to your host computer)

---

## 🪟 Windows Installation

### 1. Manual Setup
Open **PowerShell** in the project folder:
```powershell
# Create Virtual Environment
python -m venv venv

# Activate Environment (bypass execution policy if needed)
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\venv\Scripts\Activate.ps1

# Install Dependencies
pip install Flask Flask-SQLAlchemy

```

### 2. Run in Background (Headless)

To run the app without a visible terminal window, create `silent_start.vbs` in the project folder:

```vbs
Set oShell = CreateObject("WScript.Shell")
oShell.Run "python app.py", 0, False

```

### 3. Firewall Access

* Go to **Windows Defender Firewall** > **Allow an app through firewall**.
* Ensure `python.exe` has access to **Private** and **Public** networks.

---

## 🍎 macOS Installation

### 1. Manual Setup

Open **Terminal** in the project folder:

```bash
# Create and activate environment
python3 -m venv venv
source venv/bin/activate

# Install Dependencies
pip install Flask Flask-SQLAlchemy

```

### 2. Automatic Background Service (Launchd)

To have the app start automatically on boot, create a `.plist` file in `~/Library/LaunchAgents/com.raza.shiftlog.plist`:

```bash
launchctl load ~/Library/LaunchAgents/com.raza.shiftlog.plist

```

---

## 🐧 Linux Installation

### 1. Manual Setup

```bash
sudo apt update
sudo apt install python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
pip install Flask Flask-SQLAlchemy

```

### 2. Systemd Service (Production Mode)

Create a service file at `/etc/systemd/system/shiftlog.service`:

```ini
[Unit]
Description=ShiftLog Flask App
After=network.target

[Service]
User=your_username
WorkingDirectory=/path/to/shiftlog_app
ExecStart=/path/to/shiftlog_app/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target

```

Enable it with: `sudo systemctl enable --now shiftlog`

---

## 📂 Application Structure

```text
shiftlog_app/
├── app.py              # Main logic, Database models, & Route Security
├── shiftlog.db         # SQLite database (auto-generated)
└── templates/          # HTML Templates (iOS Styled)
    ├── index.html      # Shift Log Entry Form
    ├── view.html       # Monthly/Weekly History Dashboard
    └── admin.html      # Records Management

```

---

## 🔒 Security & Customization

### The Secret Key URL

The app utilizes "Security through Obscurity." The root URL (`/`) is disabled. You must access the app via a secret path defined in `app.py`:

```python
SECRET_KEY = "shift77" 

```

**Accessing on Mobile:**

1. Find your host IP (Run `ipconfig` on Windows or `ifconfig` on Mac).
2. URL: `http://192.168.x.x:8000/shift77`
3. **Important:** Bookmark this as "Add to Home Screen" in Safari for the full app experience.

---

## 🧹 Maintenance

To clear the database or start fresh, simply delete the `shiftlog.db` file. The application will recreate an empty database on the next launch.

```

### Next Step: GitHub Readiness
Since you are preparing for GitHub, the final thing you need is a `.gitignore` file. This tells GitHub **not** to upload your actual work data (`shiftlog.db`) or the large `venv` folder.

**Would you like me to generate that `.gitignore` file for you?**

```