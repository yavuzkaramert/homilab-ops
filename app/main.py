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
        "message": random.choice(QUOTES),
        "node_name": os.getenv("NODE_NAME", "unknown-node"),
        "pod_namespace": os.getenv("POD_NAMESPACE", "default")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}