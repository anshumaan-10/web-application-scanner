# config.py
import os

class Config:
    SCAN_PORT = os.getenv('SCAN_PORT', 8888)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
