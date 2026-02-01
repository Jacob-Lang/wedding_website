FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app

# Setup the environment
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
RUN uv pip install gunicorn

# CREATE THE DATA FOLDER
RUN mkdir -p /app/data

# Copy the rest of the code
COPY . .

# Run the app
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
