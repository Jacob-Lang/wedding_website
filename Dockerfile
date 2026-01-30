# Use the official uv image for a high-speed build
FROM ghcr.io/astral-sh/uv:python3.11-alpine

# Set the working directory
WORKDIR /app

# Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1

# Copy only the configuration files first to cache dependencies
COPY pyproject.toml uv.lock ./

# Install the project dependencies (this creates a virtual environment)
RUN uv sync --frozen --no-dev

# Copy the rest of your app code
COPY . .

# Ensure the virtual environment's bin is in the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run the app with Gunicorn
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
# CMD ["ls"]
