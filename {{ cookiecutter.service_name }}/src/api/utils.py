import os
from datetime import datetime
from flask import jsonify
from flask import make_response
from flask import request
from functools import wraps
from http import HTTPStatus


def construct_response(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        results = f(*args, **kwargs)

        # Construct response
        response = {
            'message': results['message'],
            'method': request.method,
            'status-code': results['status-code'],
            'timestamp': datetime.now().isoformat(),
            'url': request.url,
        }

        # Add data
        if results['status-code'] == HTTPStatus.OK:
            response['data'] = results['data']

        # Log
        logger.info(json.dumps(response, indent=4))
        return make_response(jsonify(response), response['status-code'])

    return wrap
