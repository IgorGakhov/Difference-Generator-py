import json


def render_json(diff_tree: dict) -> str:
    """
    Description:
    ---
        Rendering the diff tree to JSON format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

    Return:
    ---
        String visualization of a tree in JSON format.
    """
    return json.dumps(diff_tree, indent=4)
