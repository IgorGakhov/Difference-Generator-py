from typing import Callable
from io import TextIOWrapper
from os import path
import json

import yaml


TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')
UNSUPPORTED_TYPE = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''
FILEREAD_ERR = '''Failed to open file '{}'.
Please, check that the file path is entered correctly.'''
INVALID_FILE = '''This file is not valid.
Please, make sure the file is filled in correctly.'''


def get_data(file_path: str) -> Callable:
    """
    Description:
    ---
        Opens a file, gets the file extension, and loads the data
        as a Python dictionary.

    Parameters:
    ---
        - file_path (str): Path to file (absolute or relative).

    Return:
    ---
        data (dict): Data in the form of a Python dictionary.
    """
    return load_content(open_file(file_path), get_file_extension(file_path))


def open_file(file_path: str) -> TextIOWrapper:

    try:
        with open(file_path, 'r', encoding='utf-8') as content:
            return content.read()
    except OSError:
        raise RuntimeError(FILEREAD_ERR.format(file_path))


def get_file_extension(file_path: str) -> str:

    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower()

    return file_extension


def load_content(content: str, data_format: str) -> Callable:

    if data_format == TYPE_JSON:
        return load_json(content)
    elif data_format in TYPE_YML_OR_YAML:
        return load_yaml(content)
    else:
        raise ValueError(UNSUPPORTED_TYPE.format(data_format))


def load_json(content: str) -> dict:

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError(INVALID_FILE)


def load_yaml(content: str) -> dict:

    try:
        return yaml.load(content, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        raise RuntimeError(INVALID_FILE)
