import os
import json
import warnings

import pandas as pd

warnings.simplefilter(action="ignore", category=FutureWarning)


def load(columns: list[str]) -> dict[str, int | float]:
    """
    TODO
    :param columns:
    :return:
    """
    new_values = {}
    path = "/home/ismael/Projects/khamsat-predictor/mappers/to_numeric"

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
    TODO
    :param data_frame:
    :param columns:
    :return:
    """
    columns = [col.title() for col in columns]

    numeric_values = load(columns=columns)

    data_frame[columns] = data_frame[columns].replace(numeric_values)
    data_frame[columns] = data_frame[columns].apply(pd.to_numeric)

    return data_frame
