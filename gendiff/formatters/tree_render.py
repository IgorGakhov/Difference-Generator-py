from gendiff.formatters.stylish import render_stylish
from gendiff.constants import FORMAT_STYLISH, UNSUPPORTED_FORMAT


def visualize_diff_tree(diff_tree, format):
    if format is FORMAT_STYLISH:
        return render_stylish(diff_tree)
    else:
        raise ValueError(UNSUPPORTED_FORMAT)
