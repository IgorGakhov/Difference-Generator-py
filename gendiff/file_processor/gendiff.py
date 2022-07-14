from typing import Callable

from gendiff.file_processor.data_parser import get_data
from gendiff.file_processor.diff_assembler import get_diff_tree
from gendiff.formatters.tree_render import visualize_diff_tree
from gendiff.formatters.tree_render import DEFAULT_FORMAT


def generate_diff(file_path1: str, file_path2: str, format: str = DEFAULT_FORMAT) -> Callable:  # noqa: E501
    """
    Description:
    ---
        Accumulates all the logic of the program - accepts the entered data
        and returns the differences in the selected format.

    Parameters:
    ---
        - first_file (str): Path to first file (absolute or relative).
        - second_file (str): Path to second file (absolute or relative).

        - format (str): Format for comparison (default: stylish).

    Return:
    ---
        Visualized Difference Tree.
    """
    data1, data2 = get_data(file_path1), get_data(file_path2)

    return visualize_diff_tree(get_diff_tree(data1, data2), format)
