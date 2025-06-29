from fastapi import APIRouter, Depends, HTTPException, Request
from ..models.schemas import BatchPredictRequest

router = APIRouter()

def get_services(request: Request):
    return request.app.state

@router.post("/predict/batch")
def predict_batch(payload: BatchPredictRequest, services = Depends(get_services)):
    if not services.model_service.ready:
        raise HTTPException(status_code=503, detail="Model not loaded")
    preds = []
    for row in payload.rows:
        y, p = services.model_service.predict(row)
        preds.append({"prediction": y, "proba": p})
    return {"items": preds, "count": len(preds)}
