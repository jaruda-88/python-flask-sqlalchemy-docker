import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
APP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '1q2w3e4r')
    BASEDIR = BASE
    APPDIR = APP
    DEBUG = False


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True


def get_config(build_type: str):
    match build_type:
        case 'prod':
            return ProdConfig
        case 'dev':
            return DevConfig
        case 'test':
            return TestConfig

key = Config.SECRET_KEY