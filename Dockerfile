# Stage 1: Build
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Run
FROM python:3.11-slim
WORKDIR /app
# Güvenlik: Non-root user
RUN useradd -m devops
COPY --from=builder /root/.local /home/devops/.local
COPY ./app /app/app

ENV PATH=/home/devops/.local/bin:$PATH
USER devops

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]