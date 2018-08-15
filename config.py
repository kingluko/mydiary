import os


class Config():
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')


class Production(Config):
    DEBUG = False


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
    DEBUG = True


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
}
