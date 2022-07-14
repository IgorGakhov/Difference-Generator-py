from typing import Any

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UPDATED, NESTED
)


ADDED_TEMPLATE_PLAIN = "Property '{}' was added with value: {}"
REMOVED_TEMPLATE_PLAIN = "Property '{}' was removed"
UPDATED_TEMPLATE_PLAIN = "Property '{}' was updated. From {} to {}"
COMPLEX_VALUE = "[complex value]"


def generate_keymap(key: Any, diff_tree: dict, parent: str) -> dict:

    return {
        'value': diff_tree[key].get('value'),
        'node_type': diff_tree[key].get('node_type'),
        'path': parent + f'.{key}' if parent else f'{key}'
    }


def validate_data(value: Any) -> str:

    if isinstance(value, bool):
        valid_value = str(value).lower()
    elif value is None:
        valid_value = 'null'
    elif isinstance(value, int):
        valid_value = str(value)
    elif isinstance(value, dict):
        valid_value = COMPLEX_VALUE
    else:
        valid_value = f"'{str(value)}'"

    return valid_value


def render_plain(diff_tree: dict, parent: str = '', result=None) -> str:
    """
    Description:
    ---
        Rendering the diff tree to plain format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

        - parent (str): The path of the changed value
        from the parent (default: '').
        - result (list): Initial result of aggregation (default: None).

    Return:
    ---
        String visualization of a tree in plain format.
    """
    result = [] if result is None else result
    for key in diff_tree:
        keymap = generate_keymap(key, diff_tree, parent)

        if keymap['node_type'] == ADDED:
            result.append(
                ADDED_TEMPLATE_PLAIN.format(
                    keymap['path'], validate_data(keymap['value'])
                )
            )

        if keymap['node_type'] == REMOVED:
            result.append(REMOVED_TEMPLATE_PLAIN.format(keymap['path']))

        if keymap['node_type'] == UPDATED:
            result.append(
                UPDATED_TEMPLATE_PLAIN.format(
                    keymap['path'],
                    validate_data(keymap['value'].get('old')),
                    validate_data(keymap['value'].get('new'))
                )
            )

        if keymap['node_type'] == NESTED:
            render_plain(keymap['value'], keymap['path'], result)

    return "\n".join(result)
