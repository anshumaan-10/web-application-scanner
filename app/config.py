import os

class Config:
    DEBUG = os.getenv('DEBUG', False)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    SCAN_PORT = int(os.getenv('SCAN_PORT', 8888))  # Set default port to 8888

# Additional environment-specific configurations
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
