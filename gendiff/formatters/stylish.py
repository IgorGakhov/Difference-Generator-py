from gendiff.constants import REMOVED, ADDED, UNCHANGED, UPDATED
from gendiff.constants import DIFFLINE_TEMPLATE_STYLISH


def render_stylish(diff_tree, diff_depth=0):
    result = []
    indent = diff_depth * '  '
    for key in diff_tree:
        if diff_tree[key].get('status') is REMOVED:
            result.append(DIFFLINE_TEMPLATE_STYLISH.format(
                indent, '-', key, diff_tree[key].get('value')))

        elif diff_tree[key].get('status') is ADDED:
            result.append(DIFFLINE_TEMPLATE_STYLISH.format(
                indent, '+', key, diff_tree[key].get('value')))

        elif diff_tree[key].get('status') is UNCHANGED:
            result.append(DIFFLINE_TEMPLATE_STYLISH.format(
                indent, ' ', key, diff_tree[key].get('value')))

        elif diff_tree[key].get('status') is UPDATED:
            result.append(DIFFLINE_TEMPLATE_STYLISH.format(
                indent, '-', key, diff_tree[key]['value'].get('old')))
            result.append(DIFFLINE_TEMPLATE_STYLISH.format(
                indent, '+', key, diff_tree[key]['value'].get('new')))

    return '{\n' + "\n".join(result) + '\n}'
