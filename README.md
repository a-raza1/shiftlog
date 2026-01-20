# ShiftLog Pro

ShiftLog Pro is a secure, lightweight web application built with Flask and SQLAlchemy. It is designed to provide an iOS-native interface for tracking work hours, managing employers, and calculating weekly/monthly totals.

---

## 📋 Table of Contents
- [ShiftLog Pro](#shiftlog-pro)
  - [📋 Table of Contents](#-table-of-contents)
  - [🛠 Prerequisites](#-prerequisites)
  - [🚀 Quick Installation](#-quick-installation)
    - [Windows (PowerShell)](#windows-powershell)
    - [macOS / Linux (Terminal)](#macos--linux-terminal)
  - [🏃 Running the Application](#-running-the-application)
    - [Manual Start (Visible Terminal)](#manual-start-visible-terminal)
    - [Background Start (Hidden)](#background-start-hidden)
  - [📂 Application Structure](#-application-structure)
  - [🔒 Security \& Customization](#-security--customization)
    - [Access Control](#access-control)
  - [🧹 Maintenance](#-maintenance)

---

## 🛠 Prerequisites

- **Python 3.10+**
- **Pip** (Python Package Manager)
- **Local Network Access** (For mobile connectivity)

---

## 🚀 Quick Installation

The easiest way to set up the project is using the provided automation scripts.

### Windows (PowerShell)
1. Right-click the project folder and select **Open in Terminal**.
2. Run the setup script:
   ```powershell
   ./setup.ps1

```

*Note: If you get a permission error, run `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process` first.*

### macOS / Linux (Terminal)

1. Open Terminal in the project folder.
2. Make the script executable and run it:
```bash
chmod +x setup.sh
./setup.sh

```



---

## 🏃 Running the Application

Once the installation is complete, use these commands to start the server:

### Manual Start (Visible Terminal)

**Windows:**

```powershell
.\venv\Scripts\python.exe app.py

```

**macOS/Linux:**

```bash
./venv/bin/python3 app.py

```

### Background Start (Hidden)

**Windows:**
Run the `start_hidden.vbs` file created during setup.

**macOS:**

```bash
nohup ./venv/bin/python3 app.py > output.log 2>&1 &

```

---

## 📂 Application Structure

```text
shiftlog_app/
├── app.py              # Application logic and Database models
├── setup.sh            # Automation script (Mac/Linux)
├── setup.ps1           # Automation script (Windows)
├── shiftlog.db         # SQLite database (auto-generated)
├── requirements.txt    # Project dependencies
└── templates/          # UI Templates

```

---

## 🔒 Security & Customization

### Access Control

Access must be made via the secret path defined in `app.py` [Change it to your liking]:

```python
SECRET_KEY = "shift77" 

```

**Mobile Setup:**

1. Identify your host IP address (`ipconfig` on Windows, `ifconfig` on Mac).
2. On your iPhone, navigate to: `http://[HOST-IP]:8000/shift77`
3. Tap the **Share** icon and select **Add to Home Screen**.

---

## 🧹 Maintenance

To reset the application or clear all data, delete the `shiftlog.db` file. The application will initialize a new, empty database upon the next restart.

