from gendiff.constants import REMOVED, ADDED, UNCHANGED, UPDATED


def calculate_diff_sets(data1, data2):
    keys_1, keys_2 = set(data1.keys()), set(data2.keys())
    removed_keys = keys_1 - keys_2
    added_keys = keys_2 - keys_1
    all_keys = sorted(keys_1 | keys_2)

    return all_keys, added_keys, removed_keys


def get_diff_tree(data1, data2):

    all_keys, added_keys, removed_keys = calculate_diff_sets(data1, data2)

    diff_tree = {}
    for key in all_keys:

        if key in removed_keys:
            diff_tree[key] = {
                'value': data1[key],
                'status': REMOVED
            }

        elif key in added_keys:
            diff_tree[key] = {
                'value': data2[key],
                'status': ADDED
            }

        elif data1[key] == data2[key]:
            diff_tree[key] = {
                'value': data1[key],
                'status': UNCHANGED
            }

        else:
            diff_tree[key] = {
                'value': {
                    'old': data1[key],
                    'new': data2[key],
                },
                'status': UPDATED
            }

    return diff_tree
