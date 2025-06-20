FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /usr/src/app

COPY pyproject.toml .
COPY uv.lock .

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY /app .

ENV PATH="/usr/src/app/.venv/bin:$PATH"
# Run the application.
CMD ["fastapi", "run", "main.py"]