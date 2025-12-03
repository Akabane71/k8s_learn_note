FROM astral/uv:python3.12-bookworm-slim

WORKDIR /app

COPY . .
RUN uv sync

EXPOSE 80

# FastAPI + uvicorn
CMD ["uv","run","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]