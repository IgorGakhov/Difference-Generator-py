from gendiff.constants import REMOVED, ADDED, UPDATED, NESTED
from gendiff.constants import (
    ADDED_TEMPLATE_PLAIN,
    REMOVED_TEMPLATE_PLAIN,
    UPDATED_TEMPLATE_PLAIN,
    COMPLEX_VALUE
)


def get_path(key, parent: str) -> str:
    """
    Description:
    ---
        Get element path starting from parent.

    Parameters:
    ---
        - key (Any): The key for which the path is considered.
        - parent (str): The path of the changed value from the parent.

    Return:
    ---
        parent (str): Updated element path from parent.
    """
    if parent:
        return parent + f'.{key}'
    return f'{key}'


def handle_value(value) -> str:
    """
    Description:
    ---
        Processes the key value to represent in a string.

    Parameters:
    ---
        - value (Any): Assignable value.

    Return:
    ---
        Processed value (str).
    """
    if value in ('true', 'false', 'null'):
        return value
    if isinstance(value, dict):
        return COMPLEX_VALUE
    else:
        return f"'{value}'"


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
        value = diff_tree[key].get('value')
        status = diff_tree[key].get('status')
        path = get_path(key, parent)

        if status is ADDED:
            result.append(
                ADDED_TEMPLATE_PLAIN.format(
                    path, handle_value(value)
                )
            )

        if status is REMOVED:
            result.append(REMOVED_TEMPLATE_PLAIN.format(path))

        if status is UPDATED:
            result.append(
                UPDATED_TEMPLATE_PLAIN.format(
                    path,
                    handle_value(value.get('old')),
                    handle_value(value.get('new'))
                )
            )

        if status is NESTED:
            render_plain(value, path, result)

    return "\n".join(result)
