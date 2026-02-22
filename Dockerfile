# Stage 1: Build (Bağımlılıkların derlenmesi)
FROM python:3.11-slim as builder

WORKDIR /build
COPY requirements.txt .

# --user yerine direkt bir klasöre (target) install etmek kopyalamayı kolaylaştırır
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Run (Hafif ve güvenli çalışma ortamı)
FROM python:3.11-slim

# Uygulama çalışma dizini
WORKDIR /app

# Güvenlik: Uygulama kullanıcısını oluştur
RUN useradd -m -u 1000 devops

# Builder stage'den sadece kütüphaneleri al (Tertemiz bir image)
COPY --from=builder /install /usr/local

# Uygulama kodunu kopyala (Klasör yapısına dikkat: app/main.py -> /app/main.py)
COPY ./app /app

# Dosya sahipliğini devops kullanıcısına ver (Opsiyonel ama önerilir)
RUN chown -R devops:devops /app

# PATH zaten /usr/local/bin olduğu için extra ENV'ye gerek kalmaz
USER devops

# Uygulama başlatma (Modül yolunu sadeleştirdik)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]