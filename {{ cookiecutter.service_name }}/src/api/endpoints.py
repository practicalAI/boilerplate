import os
from flask import Blueprint
from flask import request
from http import HTTPStatus
import json

from api.operations import health_check
from config import BASE_DIR
from config import logger

# Define blueprint
_api = Blueprint('_api', __name__)


# Health check
@_api.route('/{{ cookiecutter.service_name }}/health', methods=['GET'])
@construct_response
def _health_check():
    """Health check."""
    # Get list of experiments
    results = health_check()
    return results
