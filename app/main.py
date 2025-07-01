from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, generate_latest, Counter, Gauge
from .routers import health, predict, info, batch
from .services.model_service import ModelService
from .telemetry import configure_logging
from . import config as cfg

log = configure_logging(cfg.LOG_LEVEL)

# Prometheus metrics
REGISTRY = CollectorRegistry()
REQUESTS = Counter("app_requests_total", "Total HTTP requests", ["method", "endpoint"], registry=REGISTRY)
READY = Gauge("app_ready", "Readiness gauge", registry=REGISTRY)

app = FastAPI(title="Minimal Deployment Pipeline", version=cfg.SERVICE_VERSION or "0.1.0")

# Attach services to app.state
app.state.model_service = ModelService(model_path=cfg.MODEL_PATH)

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

@app.get("/metrics")
def metrics():
    data = generate_latest(REGISTRY)
    return PlainTextResponse(data.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)

# Routers
app.include_router(health.router, tags=["system"])
app.include_router(info.router, tags=["system"])
app.include_router(predict.router, tags=["ml"])
app.include_router(batch.router, tags=["ml"])

@app.get("/version", tags=["system"])
def version():
    return {
        "service_version": app.version,
        "model_version": app.state.model_service.version if app.state.model_service.ready else "unloaded",
    }

@app.get("/ready", tags=["system"])
def ready():
    return {"ready": bool(app.state.model_service and app.state.model_service.ready)}


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

