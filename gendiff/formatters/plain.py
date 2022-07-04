from gendiff.constants import REMOVED, ADDED, UPDATED, NESTED
from gendiff.constants import (
    ADDED_TEMPLATE_PLAIN,
    REMOVED_TEMPLATE_PLAIN,
    UPDATED_TEMPLATE_PLAIN,
    COMPLEX_VALUE
)


def get_path(key, parent):
    if parent:
        return parent + f'.{key}'
    return f'{key}'


def handle_value(value):
    if value in ('true', 'false', 'null'):
        return value
    if isinstance(value, dict):
        return COMPLEX_VALUE
    else:
        return f"'{value}'"


def render_plain(diff_tree, parent='', result=None):

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
