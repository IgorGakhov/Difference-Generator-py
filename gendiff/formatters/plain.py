from types import NoneType
from typing import Any, Union


from gendiff.constants import REMOVED, ADDED, UPDATED, NESTED
from gendiff.constants import (
    ADDED_TEMPLATE_PLAIN,
    REMOVED_TEMPLATE_PLAIN,
    UPDATED_TEMPLATE_PLAIN,
    COMPLEX_VALUE
)


def generate_keymap(key: Any, diff_tree: dict, parent: str) -> dict:
    """
    Description:
    ---
        Calculating value, status and path from parent for a key.

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
        'status': diff_tree[key].get('status'),
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


def render_plain(diff_tree: dict, parent: str = '', result: Union[NoneType, list] = None) -> str:  # noqa: E501
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

        if keymap['status'] == ADDED:
            result.append(
                ADDED_TEMPLATE_PLAIN.format(
                    keymap['path'], validate_data(keymap['value'])
                )
            )

        if keymap['status'] == REMOVED:
            result.append(REMOVED_TEMPLATE_PLAIN.format(keymap['path']))

        if keymap['status'] == UPDATED:
            result.append(
                UPDATED_TEMPLATE_PLAIN.format(
                    keymap['path'],
                    validate_data(keymap['value'].get('old')),
                    validate_data(keymap['value'].get('new'))
                )
            )

        if keymap['status'] == NESTED:
            render_plain(keymap['value'], keymap['path'], result)

    return "\n".join(result)
