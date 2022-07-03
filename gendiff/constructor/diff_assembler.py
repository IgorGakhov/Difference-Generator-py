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


def get_diff_tree(data1, data2):  # noqa: C901

    all_keys, added_keys, removed_keys = calculate_diff_sets(data1, data2)

    diff_tree = {}
    for key in all_keys:

        if key in removed_keys:
            diff_tree[key] = {
                'value': data1[key],
                'status': REMOVED
            }
            check_nesting(diff_tree[key]['value'])

        elif key in added_keys:
            diff_tree[key] = {
                'value': data2[key],
                'status': ADDED
            }
            check_nesting(diff_tree[key]['value'])

        elif data1[key] == data2[key]:
            diff_tree[key] = {
                'value': data1[key],
                'status': UNCHANGED
            }
            check_nesting(diff_tree[key]['value'])

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff_tree[key] = {
                'value': get_diff_tree(data1[key], data2[key]),
                'status': NESTED
            }

        else:
            diff_tree[key] = {
                'value': {
                    'old': data1[key],
                    'new': data2[key],
                },
                'status': UPDATED
            }
            check_nesting(diff_tree[key]['value']['old'])
            check_nesting(diff_tree[key]['value']['new'])

    return diff_tree
