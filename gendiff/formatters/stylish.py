from typing import Any

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UNCHANGED, UPDATED, NESTED, CHILD
)


DIFFLINE_TEMPLATE = '{}  {} {}: {}'
ENDLINE_TEMPLATE = '{}    {}'
FRAME_TEMPLATE = '{{\n{}\n}}'
NESTING_INDENTATION = 4


def render_key_level(key: Any, value: Any, diff_symbol: str, diff_depth: int) -> list:  # noqa: E501

    result = []
    indent = diff_depth * ' '

    if isinstance(value, dict):
        result.extend([
            DIFFLINE_TEMPLATE.format(indent, diff_symbol, key, '{'),
            render_stylish(value, diff_depth + NESTING_INDENTATION),
            ENDLINE_TEMPLATE.format(indent, '}')
        ])

        return result

    else:
        value = validate_data(value)
        result.append(DIFFLINE_TEMPLATE.format(indent, diff_symbol, key, value))

        return result


def validate_data(value: Any) -> str:

    if isinstance(value, bool):
        valid_value = str(value).lower()
    elif value is None:
        valid_value = 'null'
    else:
        valid_value = str(value)

    return valid_value


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
