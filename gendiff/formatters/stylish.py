from gendiff.constants import REMOVED, ADDED, UNCHANGED, UPDATED, NESTED
from gendiff.constants import (
    DIFFLINE_TEMPLATE_STYLISH,
    ENDLINE_TEMPLATE_STYLISH,
    NESTING_INDENTATION
)


def compose_line(indent, diff_symbol, key, value):
    return DIFFLINE_TEMPLATE_STYLISH.format(
        indent, diff_symbol, key, value)


def render_key_level(key, value, diff_symbol, diff_depth, result):
    indent = diff_depth * ' '
    if isinstance(value, dict):
        result.append(compose_line(indent, diff_symbol, key, '{'))
        render_stylish(value, diff_depth + NESTING_INDENTATION, result)
        result.append(ENDLINE_TEMPLATE_STYLISH.format(indent, '}'))
    else:
        result.append(compose_line(indent, diff_symbol, key, value))


def render_stylish(diff_tree, diff_depth=0, result=None):

    result = [] if result is None else result
    for key in diff_tree:
        value = diff_tree[key].get('value')
        status = diff_tree[key].get('status')

        if status is REMOVED:
            render_key_level(key, value, '-', diff_depth, result)

        elif status is ADDED:
            render_key_level(key, value, '+', diff_depth, result)

        elif status is UNCHANGED or status is NESTED:
            render_key_level(key, value, ' ', diff_depth, result)

        elif status is UPDATED:
            render_key_level(
                key, value.get('old'), '-', diff_depth, result)
            render_key_level(
                key, value.get('new'), '+', diff_depth, result)

    return '{\n' + "\n".join(result) + '\n}'
