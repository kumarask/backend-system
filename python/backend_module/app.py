from fastapi import FastAPI
from backend_module.backend_wrapper import BackendWrapper
from backend_module.prometheus_metrics import start_metrics_server

app = FastAPI()
backend = BackendWrapper()

@app.on_event("startup")
def startup():
    backend.start()
    start_metrics_server()

@app.on_event("shutdown")
def shutdown():
    backend.stop()

@app.get("/")
def root():
    return {"status": "running"}
