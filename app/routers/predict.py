from fastapi import APIRouter, Depends, HTTPException, Request
from ..models.types import PredictRequest, PredictResponse

router = APIRouter()

def get_services(request: Request):
    return request.app.state

@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest, services = Depends(get_services)):
    if not services.model_service.ready:
        raise HTTPException(status_code=503, detail="Model not loaded")
    pred, proba = services.model_service.predict(payload.features)
    return PredictResponse(prediction=pred, proba=proba, model_version=services.model_service.version, request_id=payload.request_id)
