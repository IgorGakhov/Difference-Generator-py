from gendiff.constants import REMOVED, ADDED, UNCHANGED, UPDATED, NESTED


def calculate_diff_sets(data1, data2):
    keys_1, keys_2 = set(data1.keys()), set(data2.keys())
    removed_keys = keys_1 - keys_2
    added_keys = keys_2 - keys_1
    all_keys = sorted(keys_1 | keys_2)

    return all_keys, added_keys, removed_keys


def check_nesting(value):
    if isinstance(value, dict):
        for nested_key in value.keys():
            value[nested_key] = {
                'value': value[nested_key],
                'status': NESTED
            }
            check_nesting(value[nested_key]['value'])


def add_key(key, value, status, tree):
    if status is not UPDATED:
        tree[key] = {
            'value': value,
            'status': status
        }
        if isinstance(value, dict) and status is not NESTED:
            check_nesting(value)
    else:
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


def get_diff_tree(data1, data2):

    all_keys, added_keys, removed_keys = calculate_diff_sets(data1, data2)

    diff_tree = {}
    for key in all_keys:

        if key in removed_keys:
            add_key(key, data1[key], REMOVED, diff_tree)

        elif key in added_keys:
            add_key(key, data2[key], ADDED, diff_tree)

        elif data1[key] == data2[key]:
            add_key(key, data1[key], UNCHANGED, diff_tree)

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            add_key(key, get_diff_tree(
                data1[key], data2[key]), NESTED, diff_tree)

        else:
            add_key(key, [data1[key], data2[key]], UPDATED, diff_tree)

    return diff_tree
