#added after changing folder structure
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:moringa123@localhost/cynthia1'
    # SQLALCHEMY_DATA BASE_URI = 'postgresql+psycopg2://cynthia:moringa123@localhost/blog'

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    DEBUG= True

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:moringa123@localhost/cynthia_test'
        pass

class DevConfig(Config):

    DEBUG= True



#added after changing folder structure
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}