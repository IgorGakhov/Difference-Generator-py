from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json
from gendiff.constants import (
    FORMAT_STYLISH,
    FORMAT_PLAIN,
    FORMAT_JSON,
    UNSUPPORTED_FORMAT
)


def validate_data(diff_tree: dict) -> dict:
    """
    Description:
    ---
        Replaces recursively the values in the Dictionary type tree:
        - True -> "true"
        - False -> "false"
        - None -> "null"

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

    Return:
    ---
        The original tree with the values replaced.
    """
    for key in diff_tree:
        value = diff_tree.get(key)
        if type(value) is bool:
            diff_tree[key] = str(value).lower()
        if value is None:
            diff_tree[key] = 'null'
        if isinstance(value, dict):
            validate_data(value)

    return diff_tree


def visualize_diff_tree(diff_tree: dict, format: str) -> str:
    """
    Description:
    ---
        Activate the rendering function based on the selected format:
        stylish, plain or json.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.
        - format: stylish/plain/json.

    Raises:
    ---
        ValueError: Unsupported render format.

    Return:
    ---
        Calling the rendering function in the selected view.
    """
    if format == FORMAT_STYLISH:
        return render_stylish(validate_data(diff_tree))
    elif format == FORMAT_PLAIN:
        return render_plain(validate_data(diff_tree))
    elif format == FORMAT_JSON:
        return render_json(diff_tree)
    else:
        raise ValueError(UNSUPPORTED_FORMAT)
