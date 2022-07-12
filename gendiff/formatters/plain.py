from typing import Any

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UPDATED, NESTED
)


ADDED_TEMPLATE_PLAIN = "Property '{}' was added with value: {}"
REMOVED_TEMPLATE_PLAIN = "Property '{}' was removed"
UPDATED_TEMPLATE_PLAIN = "Property '{}' was updated. From {} to {}"
COMPLEX_VALUE = "[complex value]"


def generate_keymap(key: Any, diff_tree: dict, parent: str) -> dict:
    """
    Description:
    ---
        Calculating value, node type and path from parent for a key.

    Parameters:
    ---
        - key (Any): The key for which the path is considered.
        - diff_tree (dict): The difference tree.
        - parent (str): The path of the changed value from the parent.

    Return:
    ---
        keymap (dict): Key data as Python dictionary.
    """
    return {
        'value': diff_tree[key].get('value'),
        'node_type': diff_tree[key].get('node_type'),
        'path': parent + f'.{key}' if parent else f'{key}'
    }


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
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, dict):
        return COMPLEX_VALUE
    else:
        return f"'{str(value)}'"


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
