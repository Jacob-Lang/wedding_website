# --- Variables ---
IMAGE_NAME = wedding-app
CONTAINER_NAME = wedding-prod

# --- Targets ---

.PHONY: setup deploy local-build-flask local-build-docker

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
