import os
import logging.config

from {{ cookiecutter.package_name }}.utils import create_dirs
from {{ cookiecutter.package_name }}.utils import load_json

# Directories
BASE_DIR = os.path.dirname(__file__)
DATASETS_DIR = os.path.join('data')
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
EXPERIMENTS_DIR = os.path.join(BASE_DIR, 'experiments')

# Loggers
create_dirs(LOGS_DIR)
log_config = load_json(filepath=os.path.join(CONFIGS_DIR, 'logging.json'))
logging.config.dictConfig(log_config)
logger = logging.getLogger('logger')


class FlaskConfig(object):
    """Default Flask configuration."""
    SECRET_KEY = 'change-this-not-so-secret-key'


class DevelopmentConfig(FlaskConfig):
    '''Development configuration.'''
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000


class ProductionConfig(FlaskConfig):
    '''Production configuration.'''
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5000
