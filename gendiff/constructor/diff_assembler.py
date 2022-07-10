from typing import Any


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
CHILD = 'child'


def generate_setmap(data1: dict, data2: dict) -> dict:
    """
    Description:
    ---
        Processes data from dictionaries and generates sets
        of key intersections.

    Parameters:
    ---
        - data1 (dict): Data of the first file as a Python dictionary.
        - data2 (dict): Data of the second file as a Python dictionary.

    Return:
    ---
        setmap (dict): Sets dictionary of key intersections.
    """
    dataset_1, dataset_2 = set(data1.keys()), set(data2.keys())

    return {
        'removed_keys': dataset_1 - dataset_2,
        'added_keys': dataset_2 - dataset_1,
        'all_keys': sorted(dataset_1 | dataset_2)
    }


def add_node(status: str, value: Any, old_value: Any = None) -> dict:
    """
    Description:
    ---
        Adds data about the key (node) from the combined set to pass
        to the difference tree.

    Parameters:
    ---
        - status (str): Assignable status.
        - value (Any): Assignable value.

        - old_value (Any): Assignable old value (default: None).

    Return:
    ---
        node (dict): Data dictionary about the key (values and status).
    """
    if status == UPDATED:

        node = {
            'value': {
                'old': old_value,
                'new': value
            },
            'status': status
        }

        if isinstance(old_value, dict):
            node['value']['old'] = identify_child(node['value']['old'])

    else:

        node = {
            'value': value,
            'status': status
        }

    if isinstance(value, dict) and status != NESTED:
        if status == UPDATED:
            node['value']['new'] = identify_child(node['value']['new'])
        else:
            node['value'] = identify_child(node['value'])

    return node


def identify_child(value: dict) -> dict:
    """
    Description:
    ---
        Assigns values and status to children elements.

    Parameters:
    ---
        - value (dict): Meaning for recursive processing.

    Return:
    ---
        child (dict): Processed nested elements for value.
    """
    child = {}
    for nested_key in value.keys():
        child[nested_key] = add_node(CHILD, value.get(nested_key))

    return child


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
    setmap = generate_setmap(data1, data2)

    diff_tree = {}
    for key in setmap['all_keys']:

        if key in setmap['removed_keys']:
            diff_tree[key] = add_node(REMOVED, data1[key])

        elif key in setmap['added_keys']:
            diff_tree[key] = add_node(ADDED, data2[key])

        elif data1[key] == data2[key]:
            diff_tree[key] = add_node(UNCHANGED, data1[key])

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff_tree[key] = add_node(NESTED, get_diff_tree(data1[key], data2[key]))  # noqa: E501

        else:
            diff_tree[key] = add_node(UPDATED, data2[key], old_value=data1[key])

    return diff_tree
