import os, joblib
from sklearn.metrics import classification_report
from .data_prep import load_dataset

ARTIFACT_PATH = os.environ.get("MODEL_PATH", "model/artifacts/model.joblib")

def main():
    (_, _), (X_test, y_test) = load_dataset()
    artifact = joblib.load(ARTIFACT_PATH)
    model = artifact["model"]
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
