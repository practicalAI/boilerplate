import os
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from http import HTTPStatus

from config import DevelopmentConfig
from config import ProductionConfig
from api.endpoints import _api
from api.utils import construct_response

# Define Flask app
application = Flask(__name__)
application.url_map.strict_slashes = False
application.config['JSON_SORT_KEYS'] = False

# Configurations
config = {
    "dev": "config.DevelopmentConfig",
    "prod": "config.ProductionConfig",
}
config_name = os.getenv('ENV', 'dev')
application.config.from_object(config[config_name])

# Register blueprints
application.register_blueprint(_api)

# BAD_REQUEST
@application.errorhandler(400)
@construct_response
def bad_request(error):
    """Redirect all bad requests."""
    results = {
        "message": HTTPStatus.BAD_REQUEST.phrase,
        "status-code": HTTPStatus.BAD_REQUEST,
    }
    return results

# NOT_FOUND
@application.errorhandler(404)
@construct_response
def not_found(error):
    """Redirect all nonexistent URLS."""
    results = {
        "message": HTTPStatus.NOT_FOUND.phrase,
        "status-code": HTTPStatus.NOT_FOUND,
    }
    return results

# INTERNAL_SERVER_ERROR
@application.errorhandler(500)
@construct_response
def internal_server_error(error):
    """Internal server error."""
    results = {
        "message": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
        "status-code": HTTPStatus.INTERNAL_SERVER_ERROR,
    }
    return results
