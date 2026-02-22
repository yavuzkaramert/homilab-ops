from fastapi import FastAPI
import random
import os
import socket

app = FastAPI(
    title="The Homilab",
    description="Homelab Oracle - Konteyner Bilgelik Servisi",
    version="3.0.0"
)

# Sözleri bir değişkene alıp yönetmek iyidir
QUOTES = [
    "Konteynerlerin huzur içinde çalışıyor.",
    "Bugün bir YAML hatası yapmayacaksın, hissediyorum.",
    "CPU sıcaklığın düşük, keyfin yüksek olsun.",
    "Load Balancer bugün seni çok seviyor.",
    "Unutma: En iyi kod, silinmiş koddur. UNUTMA!",
    "BEN VARIM YANINDA..."
]

@app.get("/")
def read_root():
    """Ana dizin: Uygulama durumu ve rastgele bir motivasyon mesajı döner."""
    return {
        "status": "online",
        "version": "v3.0",
        "message": random.choice(QUOTES),
        "hostname": socket.gethostname(), # Hangi podun yanıt verdiğini görmek için kritik!
        "environment": os.getenv("APP_ENV", "development")
    }

@app.get("/health")
def health_check():
    """Kubernetes Liveness ve Readiness probları için standart endpoint."""
    return {"status": "healthy", "service": "homelab-oracle"}