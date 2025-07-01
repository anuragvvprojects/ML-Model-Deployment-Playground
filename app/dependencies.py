from fastapi import Request

def get_state(request: Request):
    return request.app.state
    
    
@app.on_event("startup")
def on_startup():
    log.info("startup", env=cfg.APP_ENV)
    try:
        app.state.model_service.load()
        READY.set(1)
        log.info("model_loaded", model_path=cfg.MODEL_PATH, version=app.state.model_service.version)
    except Exception as e:
        READY.set(0)
        log.error("model_load_failed", error=str(e), model_path=cfg.MODEL_PATH)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        response = await call_next(request)
        endpoint = request.url.path
        REQUESTS.labels(method=request.method, endpoint=endpoint).inc()
        return response
    finally:
        pass

