from gendiff.constants import REMOVED, ADDED, UNCHANGED, UPDATED, NESTED


def add_key(key, value, status: str, tree: dict):
    """
    Description:
    ---
        Adds a key from the union set to the diff tree.\n
        Uses add_unupdated_key and add_updated_key
        in itself depending on status.

    Parameters:
    ---
        - key (Any): Key to be added to the tree.
        - value (Any): Assignable value.
        - status (str): Assignable status.
        - tree (dict): The tree to which the change is being made.
    """
    if status is not UPDATED:
        add_unupdated_key(key, value, status, tree)
    else:
        add_updated_key(key, value, tree)


def add_unupdated_key(key, value, status: str, tree: dict):
    """
    Description:
    ---
        Adds unupdated key from the union set to the diff tree.

    Parameters:
    ---
        - key (Any): Key to be added to the tree.
        - value (Any): Assignable value.
        - status (str): Assignable status.
        - tree (dict): The tree to which the change is being made.
    """
    tree[key] = {
        'value': value,
        'status': status
    }
    if isinstance(value, dict) and status is not NESTED:
        check_nesting(value)


def add_updated_key(key, value, tree: dict):
    """
    Description:
    ---
        Adds updated key from the union set to the diff tree.

    Parameters:
    ---
        - key (Any): Key to be added to the tree.
        - value (Any): Assignable value.
        - tree (dict): The tree to which the change is being made.
    """
    tree[key] = {
        'value': {
            'old': value[0],
            'new': value[1],
        },
        'status': UPDATED
    }
    if isinstance(value[0], dict):
        check_nesting(value[0])
    if isinstance(value[1], dict):
        check_nesting(value[1])


def check_nesting(value):
    """
    Description:
    ---
        Assigns value and status to nested values.

    Parameters:
    ---
        - value (Any): Meaning for recursive processing.

    Return:
    ---
        Processed nested elements for value.
    """
    for nested_key in value.keys():
        value[nested_key] = {
            'value': value.get(nested_key),
            'status': NESTED
        }
        if isinstance(value[nested_key]['value'], dict):
            check_nesting(value[nested_key]['value'])


def get_diff_tree(data1: dict, data2: dict) -> dict:
    """
    Description:
    ---
        Accepts two dictionaries as input and makes a difference tree.

    Parameters:
    ---
        - data1 (str): Data of the first file as a Python dictionary.
        - data2 (str): Data of the second file as a Python dictionary.

    Return:
    ---
        diff_tree (dict): The difference tree of the first file (data1)
        and the second file (data2).
    """
    dataset_1, dataset_2 = set(data1.keys()), set(data2.keys())

    diff_tree = {}
    for key in sorted(dataset_1 | dataset_2):

        if key in dataset_1 - dataset_2:
            add_key(key, data1[key], REMOVED, diff_tree)

        elif key in dataset_2 - dataset_1:
            add_key(key, data2[key], ADDED, diff_tree)

        elif data1[key] == data2[key]:
            add_key(key, data1[key], UNCHANGED, diff_tree)

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            add_key(key, get_diff_tree(
                data1[key], data2[key]), NESTED, diff_tree)

        else:
            add_key(key, [data1[key], data2[key]], UPDATED, diff_tree)

    return diff_tree
