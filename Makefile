# --- Variables ---
IMAGE_NAME = wedding-app
CONTAINER_NAME = wedding-prod

# --- Targets ---

.PHONY: setup build run stop restart logs local-run clean

setup:
	uv sync
	mkdir -p instance
	@echo "Action Required: Copy .env.example to .env and .env.docker.example to .env.docker, generate secret key and choose passwords"

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the container in detached mode
run:
	docker run -d \
		-p 8000:8080 \
		--env-file .env.docker \
		-v $$(pwd)/instance:/app/data \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)

# Stop and remove the container (|| true prevents error if it's already stopped)
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Shortcut to rebuild and restart
restart: stop build run

# View live logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Run locally using uv (for development)
local-run:
	uv run app.py

# Remove Docker artifacts to save space
clean:
	docker system prune -f
