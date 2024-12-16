import os
from json import load

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mappers", "to_categorical"))
path = os.path.join(root, "feature_names.json")


def get_names() -> dict[str, str]:
    """
    Loads and returns the feature name mappings from a JSON file.

    :return: a dictionary containing feature name mappings
    """
    with open(path, "r", encoding="utf-8") as file:
        mapping = load(file)

    return mapping
