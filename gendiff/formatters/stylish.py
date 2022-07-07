from gendiff.constants import REMOVED, ADDED, UNCHANGED, UPDATED, NESTED
from gendiff.constants import (
    DIFFLINE_TEMPLATE_STYLISH,
    ENDLINE_TEMPLATE_STYLISH,
    NESTING_INDENTATION
)


def compose_line(indent: str, diff_symbol: str, key, value) -> str:
    """
    Description:
    ---
        Filling the String Template with Data.

    Parameters:
    ---
        - indent (str): Indent before insignia.
        - diff_symbol (str): Insignia to form a string.
        - key (Any): Key to be added to the tree.
        - value (Any): Assignable value.

    Return:
    ---
        Generated string to output (str).
    """
    return DIFFLINE_TEMPLATE_STYLISH.format(
        indent, diff_symbol, key, value)


def render_key_level(key, value, diff_symbol: str, diff_depth: int, result: list):  # noqa: E501
    """
    Description:
    ---
        Implements a string representation of a key and its value.

    Parameters:
    ---
        - key (Any): Key to be added to the tree.
        - value (Any): Assignable value.
        - diff_symbol (str): Insignia to form a string.
        - diff_depth (int): Indentation value for a line.
        - result (list): Initial result of aggregation.

    Return:
    ---
        Calling the compose_line() function.
    """
    indent = diff_depth * ' '
    if isinstance(value, dict):
        result.append(compose_line(indent, diff_symbol, key, '{'))
        render_stylish(value, diff_depth + NESTING_INDENTATION, result)
        result.append(ENDLINE_TEMPLATE_STYLISH.format(indent, '}'))
    else:
        result.append(compose_line(indent, diff_symbol, key, value))


def render_stylish(diff_tree: dict, diff_depth: int = 0, result=None) -> str:
    """
    Description:
    ---
        Rendering the diff tree to stylish format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

        - diff_depth (int): Indentation value for a line (default: 0).
        - result (list): Initial result of aggregation (default: None).

    Return:
    ---
        String visualization of a tree in stylish format.
    """
    result = [] if result is None else result
    for key in diff_tree:
        value = diff_tree[key].get('value')
        status = diff_tree[key].get('status')

        if status is REMOVED:
            render_key_level(key, value, '-', diff_depth, result)

        elif status is ADDED:
            render_key_level(key, value, '+', diff_depth, result)

        elif status is UNCHANGED or status is NESTED:
            render_key_level(key, value, ' ', diff_depth, result)

        elif status is UPDATED:
            render_key_level(
                key, value.get('old'), '-', diff_depth, result)
            render_key_level(
                key, value.get('new'), '+', diff_depth, result)

    return '{\n' + "\n".join(result) + '\n}'
