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

## 🔒 Private Config

Wedding details (date, venue, meal options) live in `wedding_config.json`, which is gitignored. Copy `wedding_config.example.json` to get started:

```bash
cp wedding_config.example.json wedding_config.json
# then fill in your real details
```

### Deploying config to your VPS

`wedding_config.json` is never pushed to git, so copy it to your server manually with `scp`:

```bash
scp wedding_config.json user@your-vps-ip:/path/to/wedding_website/wedding_config.json
```

For example:
```bash
scp wedding_config.json jacob@123.456.789.0:~/wedding_website/wedding_config.json
```

Then restart the app on the VPS so it picks up the new config:
```bash
ssh user@your-vps-ip "cd ~/wedding_website && docker compose up -d --build"
```
