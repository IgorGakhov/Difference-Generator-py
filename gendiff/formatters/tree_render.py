from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json
from gendiff.constants import (
    FORMAT_STYLISH,
    FORMAT_PLAIN,
    FORMAT_JSON,
    UNSUPPORTED_FORMAT
)


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
        return render_stylish(diff_tree)
    elif format == FORMAT_PLAIN:
        return render_plain(diff_tree)
    elif format == FORMAT_JSON:
        return render_json(diff_tree)
    else:
        raise ValueError(UNSUPPORTED_FORMAT)
