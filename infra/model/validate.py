import os, joblib, sys
path = os.environ.get("MODEL_PATH", "model/artifacts/model.joblib")
artifact = joblib.load(path)
assert "model" in artifact and "version" in artifact
print("OK:", artifact.get("version"))
