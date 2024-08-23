# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app

ENV SCAN_PORT=8888

EXPOSE 8888

CMD ["python", "scanner.py"]
