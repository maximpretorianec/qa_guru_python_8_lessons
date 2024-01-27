import json, os

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schemas'))


def load_schema(filename):
    with open(os.path.join(resources_path, filename)) as file:
        schema = json.load(file)
        return schema
