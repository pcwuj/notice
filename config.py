class Config(object):
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = ''
    USER = ''
    PASSWORD = ''
    DATABASE = ''
    DISTRIBUTE_DATABASE = ''
    SQLALCHEMY_DATABASE_URI = ''
    JSONIFY_MIMETYPE = 'application/json;charset=utf-8'
    JSON_AS_ASCII = False


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True


# 测试环境
class TestConfig(Config):
    DEBUG = False


# 生产环境
class ProductionConfig(Config):
    DEBUG = False


# 配置的字典
configDict = {
    # 'default': DevelopmentConfig('prod'),
    # 'dev': DevelopmentConfig('dev'),
    # 'test': TestConfig('test'),
    'prod': ProductionConfig()
}
