import pandas as pd
from fastapi import APIRouter

from mappers import to_numeric
from models import Request

router = APIRouter(prefix="/offer", tags=["Offer"])


@router.post(path="/", summary="Enter The Offer Features")
def predict(request: Request):
    data = request.model_dump()
    data = to_numeric(pd.DataFrame([data]), columns=["duration", "offer_response_time", "owner_response_time"])
    data = data.to_dict(orient="records")

    return data
