from gendiff.constructor.data_parser import get_data
from gendiff.constructor.diff_assembler import get_diff_tree
from gendiff.formatters.tree_render import visualize_diff_tree
from gendiff.constants import DEFAULT_FORMAT


def generate_diff(file_path1, file_path2, format=DEFAULT_FORMAT):
    data1, data2 = get_data(file_path1), get_data(file_path2)

    return visualize_diff_tree(get_diff_tree(data1, data2), format)
