import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitches'
    SECRET_KEY = 'BDSFHEWFIUEDABJCVZMCbmDKJDjb'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    pass

class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}