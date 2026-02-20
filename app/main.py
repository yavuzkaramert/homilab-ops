from fastapi import FastAPI
import random
import os

app = FastAPI(title="The Homilab")

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
    return {
        "status": "online",
        "message": "Test v1.0 - Konteynerler çalışıyor, her şey yolunda!"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}