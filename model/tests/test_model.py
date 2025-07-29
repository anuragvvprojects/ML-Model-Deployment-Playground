import os, joblib

def test_model_artifact_exists():
    path = os.environ.get("MODEL_PATH", "model/artifacts/model.joblib")
    art = joblib.load(path)
    assert "model" in art and "version" in art
