from pydantic import BaseModel, Field
from typing import List, Optional

class PredictRequest(BaseModel):
    features: List[float] = Field(..., description="Numerical feature vector for the model.")
    request_id: Optional[str] = Field(default=None, description="Optional correlation id")

class PredictResponse(BaseModel):
    prediction: int
    proba: float
    model_version: str
    request_id: Optional[str] = None
    
    
    
class PredictRequest(BaseModel):
    features: List[float] = Field(..., description="Numerical feature vector for the model.")
    request_id: Optional[str] = Field(default=None, description="Optional correlation id")


class PredictRequest(BaseModel):
    features: List[float] = Field(..., description="Numerical feature vector for the model.")
    request_id: Optional[str] = Field(default=None, description="Optional correlation id")

