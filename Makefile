# --- Variables ---
IMAGE_NAME = wedding-app
CONTAINER_NAME = wedding-prod

# --- Targets ---

.PHONY: setup deploy local-build-flask local-build-docker db-init db-migrate db-upgrade

setup:
	uv sync
	mkdir -p data
	flask db init
	@echo "Action Required: Copy .env.example to .env and .env.docker.example to .env.docker, generate secret key and choose passwords"

# Pull recent code changes and add
deploy:
	git pull origin main
	docker compose up -d --build
	docker image prune -f

# Run locally using uv (for development)
local-build-flask:
	uv run app.py

local-build-docker:
	docker compose up --build

# 1. Run this ONLY ONCE on your local machine to start the system
db-init:
	flask db init

# Run this locally whenever you change your models.py / db.Model
# Usage: make migrate msg="added dietary requirements"
db-migrate:
	flask db migrate -m "$(msg)"

# 3. Run this locally AND on the VPS to apply the changes
db-upgrade:
	flask db upgrade
