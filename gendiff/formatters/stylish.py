from typing import Any

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UNCHANGED, UPDATED, NESTED, CHILD
)


DIFFLINE_TEMPLATE = '{}  {} {}: {}'
ENDLINE_TEMPLATE = '{}    {}'
FRAME_TEMPLATE = '{{\n{}\n}}'
NESTING_INDENTATION = 4


def render_key_level(key: Any, value: Any, diff_symbol: str, diff_depth: int) -> list:  # noqa: E501
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

    Return:
    ---
        result (list): List of rendered lines.
    """
    result = []
    indent = diff_depth * ' '

    if isinstance(value, dict):
        result.extend([
            compose_line(indent, diff_symbol, key, '{'),
            render_stylish(value, diff_depth + NESTING_INDENTATION),
            ENDLINE_TEMPLATE.format(indent, '}')
        ])

        return result

    else:
        value = validate_data(value)
        result.append(compose_line(indent, diff_symbol, key, value))

        return result


def compose_line(indent: str, diff_symbol: str, key: Any, value: Any) -> str:
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
    return DIFFLINE_TEMPLATE.format(indent, diff_symbol, key, value)


def validate_data(value: Any) -> str:
    """
    Description:
    ---
        Replaces values:
        - True -> "true"
        - False -> "false"
        - None -> "null"

        It then processes the key value to represent in the string.

    Parameters:
    ---
        - value (Any): Assignable value.

    Return:
    ---
        value (str): Processed value.
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def render_stylish(diff_tree: dict, diff_depth: int = 0) -> str:
    """
    Description:
    ---
        Rendering the diff tree to stylish format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

        - diff_depth (int): Indentation value for a line (default: 0).

    Return:
    ---
        result (str): String visualization of a tree in stylish format.
    """
    result = []

    for key in diff_tree:
        value = diff_tree[key].get('value')
        node_type = diff_tree[key].get('node_type')

        if node_type == REMOVED:
            result.extend(render_key_level(key, value, '-', diff_depth))

        elif node_type == ADDED:
            result.extend(render_key_level(key, value, '+', diff_depth))

        elif node_type in (UNCHANGED, NESTED, CHILD):
            result.extend(render_key_level(key, value, ' ', diff_depth))

        elif node_type == UPDATED:
            result.extend(render_key_level(key, value.get('old'), '-', diff_depth))  # noqa: E501
            result.extend(render_key_level(key, value.get('new'), '+', diff_depth))  # noqa: E501

    result = '\n'.join(result)
    return FRAME_TEMPLATE.format(result) if diff_depth == 0 else result
