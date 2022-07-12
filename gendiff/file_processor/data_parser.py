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


def open_file(file_path: str):
    """
    Description:
    ---
        File Opener.

    Parameters:
    ---
        - file_path (str): Path to file (absolute or relative).

    Raises:
    ---
        RuntimeError: Failed to open file.

    Return:
    ---
        content (str): Data from a file as a string.
        file_extension (str): File extension.
    """
    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower()

    try:
        with open(file_path, 'r', encoding='utf-8') as content:
            return content.read(), file_extension
    except OSError:
        raise RuntimeError(FILEREAD_ERR.format(file_path))


def load_content(content: str, file_extension: str):
    """
    Description:
    ---
        File Content Loader.

    Parameters:
    ---
        - content (str): Data from a file as a string.
        - file_extension (str): File extension.

    Raises:
    ---
        ValueError: Unsupported file extension.

    Return:
    ---
        data (dict): Loads data as a Python dictionary.
    """
    if file_extension == TYPE_JSON:
        return load_json(content)
    elif file_extension in TYPE_YML_OR_YAML:
        return load_yaml(content)
    else:
        raise ValueError(UNSUPPORTED_TYPE.format(file_extension))


def load_json(content: str) -> dict:
    """
    Description:
    ---
        JSON File Converter.

    Parameters:
    ---
        - content (str): Data from a file as a string.

    Raises:
    ---
        RuntimeError: This file is not valid.

    Return:
    ---
        data (dict): Converts JSON document to Python dictionary object.
    """
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError(INVALID_FILE)


def load_yaml(content: str) -> dict:
    """
    Description:
    ---
        YML/YAML File Converter.

    Parameters:
    ---
        - content (str): Data from a file as a string.

    Raises:
    ---
        RuntimeError: This file is not valid.

    Return:
    ---
        data (dict): Converts YML/YAML document to Python dictionary object.
    """
    try:
        return yaml.load(content, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        raise RuntimeError(INVALID_FILE)


def get_data(file_path: str) -> dict:
    """
    Description:
    ---
        Processes the file path and returns the data as a Python dictionary.

    Parameters:
    ---
        - file_path (str): Path to file (absolute or relative).

    Return:
    ---
        data (dict): Data in the form of a Python dictionary.
    """
    content, file_extension = open_file(file_path)

    return load_content(content, file_extension)
