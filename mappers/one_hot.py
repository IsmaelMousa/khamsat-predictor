import os
from json import load

import numpy as np

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mappers", "to_numeric"))


def get_keys(column: str) -> list[str]:
    """
    TODO
    :param column:
    :return:
    """
    file_name = column.lower().replace(" ", "_") + ".json"
    file_path = os.path.join(root, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        mapping = load(file)

    return mapping.keys()


def encode(value: str, column: str) -> np.ndarray:
    """
    TODO
    :param value:
    :param column:
    :return:
    """
    file_name = column.lower().replace(" ", "_") + ".json"
    file_path = os.path.join(root, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        mapping = load(file)

    vector = np.zeros(len(mapping))

    vector[mapping[value]] = 1

    return vector
