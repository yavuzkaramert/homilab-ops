from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import socket
import datetime

app = FastAPI(title="Homelab Hello World")

@app.get("/", response_class=HTMLResponse)
async def root():
    # Sistem bilgilerini alalım (Pod adı ve zaman)
    hostname = socket.gethostname()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Basit ama şık bir CSS ile görselleştirelim
    html_content = f"""
    <html>
        <head>
            <title>Raspberry Pi Homelab</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #1a1a2e;
                    color: #e94560;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .card {{
                    background-color: #16213e;
                    padding: 2rem;
                    border-radius: 15px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                    border: 1px solid #0f3460;
                    text-align: center;
                }}
                h1 {{ color: #4ecca3; margin-bottom: 0.5rem; }}
                p {{ color: #95a5a6; font-size: 1.1rem; }}
                .status {{
                    display: inline-block;
                    padding: 5px 15px;
                    background-color: #4ecca3;
                    color: #1a1a2e;
                    border-radius: 20px;
                    font-weight: bold;
                    margin-top: 10px;
                }}
                .hostname {{ font-family: monospace; color: #f8b400; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 Homelab Status</h1>
                <p>Uygulama başarıyla çalışıyor!</p>
                <div class="status">ONLINE</div>
                <hr style="border: 0.5px solid #0f3460; margin: 20px 0;">
                <p><b>Pod Hostname:</b> <span class="hostname">{hostname}</span></p>
                <p><b>Sistem Saati:</b> {now}</p>
            </div>
        </body>
    </html>
    """
    return html_content

@app.get("/health")
async def health_check():
    # Kubernetes Liveness/Readiness probe'ları için gerekli
    return {"status": "healthy", "timestamp": datetime.datetime.now()}