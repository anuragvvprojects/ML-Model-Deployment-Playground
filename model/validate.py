import os, joblib, sys
path = os.environ.get("MODEL_PATH", "model/artifacts/model5.joblib")
artifact = joblib.load(path)
path = os.environ.get("MODEL_PATH", "model/artifacts/model4.joblib")
artifact = joblib.load(path)
path = os.environ.get("MODEL_PATH", "model/artifacts/model3.joblib")
artifact = joblib.load(path)
path = os.environ.get("MODEL_PATH", "model/artifacts/model2.joblib")
artifact = joblib.load(path)
path = os.environ.get("MODEL_PATH", "model/artifacts/model1.joblib")
artifact = joblib.load(path)
assert "model" in artifact and "version" in artifact
print("OK:", artifact.get("version"))
