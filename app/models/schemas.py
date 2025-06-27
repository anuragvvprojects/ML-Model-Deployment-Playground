from pydantic import BaseModel, Field
from typing import List

class BatchPredictRequest(BaseModel):
    rows: List[List[float]] = Field(..., description="2D array of feature rows")
