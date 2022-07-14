from typing import Any


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
CHILD = 'child'


def get_diff_tree(data1: dict, data2: dict) -> dict:
    """
    Description:
    ---
        Accepts two dictionaries as input and makes a difference tree.

    Parameters:
    ---
        - data1 (dict): Data of the first file as a Python dictionary.
        - data2 (dict): Data of the second file as a Python dictionary.

    Return:
    ---
        diff_tree (dict): The difference tree of the first file (data1)
        and the second file (data2).
    """
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_tree = {}
    for key in all_keys:

        if key in data1 and key not in data2:
            diff_tree[key] = add_node(REMOVED, data1[key])

        elif key not in data1 and key in data2:
            diff_tree[key] = add_node(ADDED, data2[key])

        elif data1[key] == data2[key]:
            diff_tree[key] = add_node(UNCHANGED, data1[key])

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff_tree[key] = add_node(NESTED, get_diff_tree(data1[key], data2[key]))  # noqa: E501

        else:
            diff_tree[key] = add_node(UPDATED, data2[key], old_value=data1[key])

    return diff_tree


def add_node(node_type: str, value: Any, old_value: Any = None) -> dict:

    if node_type == UPDATED:

        node = {
            'value': {
                'old': old_value,
                'new': value
            },
            'node_type': node_type
        }

        if isinstance(old_value, dict):
            node['value']['old'] = identify_child(node['value']['old'])

    else:

        node = {
            'value': value,
            'node_type': node_type
        }

    if isinstance(value, dict) and node_type != NESTED:
        if node_type == UPDATED:
            node['value']['new'] = identify_child(node['value']['new'])
        else:
            node['value'] = identify_child(node['value'])

    return node


def identify_child(value: dict) -> dict:

    child = {}
    for nested_key in value.keys():
        child[nested_key] = add_node(CHILD, value.get(nested_key))

    return child
