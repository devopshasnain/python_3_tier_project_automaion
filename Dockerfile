FROM python:3.11-slim

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# MySQL dependency
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

# Python deps (cache friendly)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Non-root user
RUN adduser --disabled-password appuser

# ✅ Explicit backend files copy

COPY app ./app
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "-m", "app.main"]
