import pandas as pd
from fastapi import APIRouter

from mappers import to_numeric, encode, get_keys
from models import Request

router = APIRouter(prefix="/offer", tags=["Offer"])
@router.post(path="/", summary="Enter the offer features to predict the price.")
def enter(request: Request):
    data = request.model_dump()

    data = to_numeric(pd.DataFrame([data]), columns=["duration", "offer_response_time", "owner_response_time", "owner_level"])

    category_encoded = pd.DataFrame(data["category_name"].apply(lambda value: encode(value=value, column="category_name")).tolist(), columns=[key for key in get_keys(column="Category Name")])
    service_encoded = pd.DataFrame(data["service_name"].apply(lambda value: encode(value=value, column="service_name")).tolist(), columns=[key for key in get_keys(column="Service Name")])

    data = data.drop(columns=["category_name", "service_name"])

    data = pd.concat(objs=[data, category_encoded, service_encoded], axis=1)

    return data.to_dict(orient="records")[0]