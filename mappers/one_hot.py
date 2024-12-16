import os
from json import load

import numpy as np

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mappers", "to_numeric"))


def get_keys(column: str) -> list[str]:
    """
    Retrieves the keys (categorical values) from the mapping JSON file for a given column.

    :param column: the name of the column to fetch keys for
    :return: a list of keys from the mapping file
    """
    file_name = column.lower().replace(" ", "_") + ".json"
    file_path = os.path.join(root, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        mapping = load(file)

    return list(mapping.keys())


def encode(value: str, column: str) -> np.ndarray:
    """
    Encodes a given value for a specified column into a one-hot vector,
    where the values set to 1 and the other set to 0.

    :param value: the value to encode
    :param column: the name of the column associated with the value
    :return: a one-hot encoded NumPy array representing the value
    """
    file_name = column.lower().replace(" ", "_") + ".json"
    file_path = os.path.join(root, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        mapping = load(file)

    vector = np.zeros(len(mapping))

    vector[mapping[value]] = 1

    return vector
