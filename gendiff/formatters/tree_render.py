from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.constants import (
    FORMAT_STYLISH,
    FORMAT_PLAIN,
    FORMAT_JSON,
    UNSUPPORTED_FORMAT
)


def visualize_diff_tree(diff_tree, format):
    if format == FORMAT_STYLISH:
        return render_stylish(diff_tree)
    elif format == FORMAT_PLAIN:
        return render_plain(diff_tree)
    elif format == FORMAT_JSON:
        pass
    else:
        raise ValueError(UNSUPPORTED_FORMAT)
