from os import path
import json
import yaml


from gendiff.constants import TYPE_JSON, TYPE_YML_OR_YAML, UNSUPPORTED_TYPE


def load_data(file_path: str, file_extension: str) -> dict:
    """
    Description:
    ---
        File Downloader.

    Parameters:
    ---
        - file_path (str): Path to file (absolute or relative).
        - file_extension (str): File extension.

    Raises:
    ---
        ValueError: Unsupported file extension.

    Return:
    ---
        data (dict): Data in the form of a Python dictionary.
    """
    with open(file_path) as file:
        if file_extension == TYPE_JSON:
            data = json.load(file)
        elif file_extension in TYPE_YML_OR_YAML:
            data = yaml.load(file, Loader=yaml.FullLoader)
        else:
            raise ValueError(UNSUPPORTED_TYPE.format(file_extension))

    return data


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
    _, file_extension = path.splitext(file_path)
    file_extension = file_extension.lower()
    data = load_data(file_path, file_extension)

    return data
