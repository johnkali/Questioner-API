""" The Configuration file for  API """

class Config(object):
    """ For thr Parent configuration class """
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """ Configuration for development environment - setting the debug to true for development"""
    DEBUG = True

class StagingConfig(Config):
    """ Config for staging the environment """
    DEBUG = True

class TestingConfig(Config):
    """ Configuration for the testing environment set to true """
    TESTING = True

class ProductionConfig(Config):
    """ The Config for the production environment """
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'debug': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}