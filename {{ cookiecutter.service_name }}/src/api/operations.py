import os
from http import HTTPStatus


def health_check():
    """Health check."""
    # Health check operations
    pass

    # Results
    results = {
        'message': HTTPStatus.OK.phrase,
        'status-code': HTTPStatus.OK,
        'data': {}
    }

    return results
