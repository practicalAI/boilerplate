import os
from flask import Blueprint
from flask import request
from http import HTTPStatus
import json

from api import utils
import config

# Define blueprint
_api = Blueprint('_api', __name__)


# Health check
@_api.route('/{{ cookiecutter.service_name }}/health', methods=['GET'])
@utils.construct_response
def _health_check():
    """Health check."""
    # Get list of experiments
    results = utils.health_check()
    return results
