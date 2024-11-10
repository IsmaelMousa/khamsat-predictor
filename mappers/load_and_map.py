import os
import json
import warnings

import pandas as pd

warnings.simplefilter(action="ignore", category=FutureWarning)


def load(columns: list[str]) -> dict[str, int | float]:
    """
    Loads numeric mappings from JSON files for the specified columns.

    :param columns: list of column names
    :return: a dictionary mapping each column to its numeric values
    """
    new_values = {}

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "mappers", "to_numeric")

    for col in columns:
        file_name = col.lower().replace(" ", "_") + ".json"

        if file_name:
            file_path = os.path.join(path, file_name)

            with open(file_path, "r") as file:
                numeric_values = json.load(file)
                new_values[col] = numeric_values

    return new_values


def to_numeric(data_frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Converts specified columns in the DataFrame to numeric values based on predefined mappings.

    :param data_frame: the dataset as a dataframe
    :param columns: list of column names
    :return: dataframe with converted columns
    """
    columns = [col.title() for col in columns]

    numeric_values = load(columns=columns)

    data_frame[columns] = data_frame[columns].replace(numeric_values)
    data_frame[columns] = data_frame[columns].apply(pd.to_numeric)

    return data_frame
