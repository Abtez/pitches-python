import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitches'
    SECRET_KEY = 'BDSFHEWFIUEDABJCVZMCbmDKJDjb'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitches_test'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://djvygrhpzklozg:c13bc83cb1b836c3e392d1bfeb78c640c11e738a57d02e4b150e9925868809db@ec2-52-73-199-211.compute-1.amazonaws.com:5432/d5lb6mp4ab5neg'

class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}