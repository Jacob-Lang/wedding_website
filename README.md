# 💍 Wedding Website

I'm getting married! Let's build a website from scratch.

A containerized Flask application designed to manage wedding guest lists and RSVPs. This project demonstrates a modern Python development workflow using **uv**, **Docker**, and **Automated Task Management**.

## 🚀 Technical Highlights
* **Backend:** Flask (Python) with SQLAlchemy.
* **Database:** SQLite (Relational storage with volume persistence).
* **Environment Management:** Managed via `uv` for lightning-fast, reproducible builds.
* **Containerization:** Fully Dockerized with optimized `.dockerignore` and multi-environment `.env` support.
* **Automation:** Comprehensive `Makefile` for streamlined development and deployment.

---

## 🛠 Prerequisites
* [uv](https://docs.astral.sh/uv/) (Python package manager)
* Docker & Docker Compose
* Make (Standard on macOS/Linux)

---

## 🏃‍♂️ Getting Started

### 1. Project Initialization
The setup command handles dependency installation and prepares the local environment:
```bash
make setup
```

### 2. Local Development
Run the application in a local virtual environment for rapid iteration:
```bash
make local-run
```
Access the UI at http://127.0.0.1:5000

### 3. Production Simulation (Docker)
Build and run the containerized version to test production behavior:

```bash
make restart
make logs
```
Access the containerized app at http://localhost:8000

---

## Project Architecture
Plaintext
├── app.py              # Main application logic
├── Makefile            # Project automation shortcuts
├── Dockerfile          # Container specification
├── instance/           # Local SQLite storage (Volume mounted)
├── templates/          # Jinja2 HTML templates
└── pyproject.toml      # Project metadata and dependencies
🔒 Security & Persistence
Data Persistence: The SQLite database is mapped to a local volume, ensuring guest data survives container restarts and upgrades.

Secret Management: Utilizes decoupled .env files for local vs. containerized secrets.

CSRF Protection: Integrated session signing via Flask Secret Keys.
