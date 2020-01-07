import os
import json


def create_dirs(dirpath):
    """Creating directories."""
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def load_json(filepath):
    """Load a json file."""
    with open(filepath, 'r') as fp:
        json_obj = json.load(fp)
    return json_obj
