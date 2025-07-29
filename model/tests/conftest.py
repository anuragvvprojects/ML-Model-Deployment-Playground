import os, importlib, pytest
from model.train import main as train_main

@pytest.fixture(scope="session")
def app_module(tmp_path_factory, monkeypatch):
    artifact = tmp_path_factory.mktemp("artifacts") / "model.joblib"
    monkeypatch.setenv("MODEL_PATH", str(artifact))
    # Train a fresh artifact for tests
    train_main()
    # Import and reload the app so it reads the env + loads the model
    import app.main as app_main
    importlib.reload(app_main)
    return app_main

@pytest.fixture()
def client(app_module):
    from fastapi.testclient import TestClient
    return TestClient(app_module.app)
