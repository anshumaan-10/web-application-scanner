import os

# Configuration settings for your application
class Config:
    DEBUG = os.getenv('DEBUG', False)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    # Add other configuration settings as needed

# Additional environment-specific configurations
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
