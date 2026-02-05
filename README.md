# 💍 Wedding Website

I'm getting married! Let's build a website from scratch.

## 🛠 Prerequisites
* uv
* Docker & Docker Compose
* Make

## 🏃‍♂️ Getting Started

### 1. Project Initialization
```bash
make setup
```

### 2. Local Development
Run the website directly as a Flask app.
```bash
make local-run
```
Access the local website at http://127.0.0.1:5000

### 3. Production Simulation (Docker)
Run the website inside a container with gunicorn.

```bash
make restart
make logs
```
Access the containerized website at http://localhost:8000
