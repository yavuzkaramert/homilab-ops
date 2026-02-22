# =========================
# Stage 1 — Builder
# =========================
FROM python:3.11-slim AS builder

WORKDIR /build

# Build için gerekli sistem paketleri
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# pip tooling upgrade
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .

# Bağımlılıkları /install altına kur
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# =========================
# Stage 2 — Runtime
# =========================
FROM python:3.11-slim

WORKDIR /app

# Non-root user
RUN useradd -m -u 1000 devops

# Builder stage’den sadece kurulu paketleri al
COPY --from=builder /install /usr/local

# Uygulama kodu
COPY ./app /app

# Sahiplik
RUN chown -R devops:devops /app

USER devops

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]