from fastapi import APIRouter

router = APIRouter()

@router.get("/version")
def version():
    # Accurate versioning is provided at /version in main; this remains for compatibility
    return {"service_version": "unknown", "model_version": "unknown"}
