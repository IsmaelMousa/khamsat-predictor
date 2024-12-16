import os

import joblib
import pandas as pd
from fastapi import APIRouter, status

from mappers import to_numeric, encode, get_keys, get_names
from models import Request, Response

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "experiments"))
model_path = os.path.join(root, "Random Forest Classifier", "0", "balanced", "artifacts", "model", "model.pkl")

model = joblib.load(model_path)

feature_names = get_names()
database = {}
router = APIRouter(prefix="/offer", tags=["Offer"])


@router.post(path="/", summary="Enter the offer features.")
def enter(request: Request) -> dict:
    """
    Stores the offer details that entered by the user after preprocessing and encoding.

    :param request: Offer details sent as a request payload
    :return: Response with status and success message
    """
    data = request.model_dump()
    data = to_numeric(pd.DataFrame([data]), columns=["duration", "offer_response_time", "owner_response_time", "owner_level"])

    category_encoded = pd.DataFrame(data["category_name"].apply(lambda value: encode(value=value, column="category_name")).tolist(), columns=[key for key in get_keys(column="Category Name")])
    service_encoded = pd.DataFrame(data["service_name"].apply(lambda value: encode(value=value, column="service_name")).tolist(), columns=[key for key in get_keys(column="Service Name")])

    data = data.drop(columns=["category_name", "service_name"])
    data = pd.concat(objs=[data, category_encoded, service_encoded], axis=1)
    data = data.rename(columns=feature_names)

    database[0] = data.to_dict(orient="records")[0]

    return Response(status=status.HTTP_201_CREATED, message="Successfully entered offer information.").model_dump()

@router.get(path="/{offer_id}", summary="Predict the price.")
def get_offer(offer_id: int) -> dict:
    """
    Predicts the price of an offer based on its features that has a corresponding offer ID.

    :param offer_id: the ID of the offer in the database
    :return: Response with status and the predicted price or an error message
    """
    if offer_id in database:
        data = pd.DataFrame([database[offer_id]])

        return Response(status=status.HTTP_200_OK, message=f"${model.predict(data).tolist()[0]}0").model_dump()

    return Response(status=status.HTTP_404_NOT_FOUND, message=f"No data found with ID {offer_id}.").model_dump()