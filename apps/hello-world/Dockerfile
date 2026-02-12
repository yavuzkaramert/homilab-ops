# Hafif bir Python imajı kullanıyoruz
FROM python:3.11-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Uygulamanın çalışacağı portu belirt
EXPOSE 8000

# Uygulamayı başlat (Production için worker sayısı optimize edilebilir)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]