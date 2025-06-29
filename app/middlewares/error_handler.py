from fastapi import Request
from fastapi.responses import JSONResponse

async def catch_all_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return JSONResponse(status_code=500, content={"detail": "internal_error"})
