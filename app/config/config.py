"""Flask configuration."""
from os import environ


class Config:
    """Base config."""
    pass


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    FIRESTORE = 'firestore_emulator:8200'


class LocalConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    FIRESTORE = 'localhost:8200'
