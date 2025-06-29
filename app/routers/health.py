from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/ready")
def ready():
    # actual readiness is provided by /ready in main with model state
    return {"ready": True}
