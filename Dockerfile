FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

COPY pyproject.toml /app/
COPY uv.lock /app/

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY . /app

ENV PATH="/app/.venv/bin:$PATH"
# Run the application.
CMD ["fastapi", "run", "main.py"]