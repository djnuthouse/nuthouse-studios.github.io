# ---------- Base Image ----------
FROM python:3.11-slim

# ---------- Environment Setup ----------
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000

WORKDIR /app

# ---------- Dependencies ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy Application ----------
COPY . .

# ---------- Expose Port ----------
EXPOSE 5000

# ---------- Run the App ----------
# Heroku detects this automatically and runs it as "web" process
CMD gunicorn --bind 0.0.0.0:$PORT src.server:app
