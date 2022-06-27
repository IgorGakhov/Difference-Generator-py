from os import path
import json
import yaml


TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')

UNSUPPORTED_FORMAT = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''


def load_data(file_path, file_extension):
    with open(file_path) as file:
        if file_extension == TYPE_JSON:
            data = json.load(file)
        elif file_extension in TYPE_YML_OR_YAML:
            data = yaml.load(file, Loader=yaml.FullLoader)
        else:
            raise ValueError(UNSUPPORTED_FORMAT.format(file_extension))

    return data


def validate_data(data):
    for key in data:
        value = data.get(key)
        if type(value) is bool:
            data[key] = str(value).lower()
        if value is None:
            data[key] = 'null'

    return data


def get_data(file_path):
    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower()
    data = validate_data(load_data(file_path, file_extension))

    return data
