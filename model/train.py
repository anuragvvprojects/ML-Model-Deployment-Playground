import os, joblib
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .data_prep import load_dataset

ARTIFACT_PATH = os.environ.get("MODEL_PATH", "model/artifacts/model.joblib")
VERSION = os.environ.get("MODEL_VERSION", "0.1.0")

def main():
    (X_train, y_train), (X_test, y_test) = load_dataset()
    clf = LogisticRegression(max_iter=1000, multi_class="auto")
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))

    artifact = {
        "model": clf,
        "version": VERSION,
        "trained_at": datetime.utcnow().isoformat(),
        "metrics": {"accuracy": acc},
    }
    os.makedirs(os.path.dirname(ARTIFACT_PATH), exist_ok=True)
    joblib.dump(artifact, ARTIFACT_PATH)
    print(f"Saved model -> {ARTIFACT_PATH} (accuracy={acc:.4f}, version={VERSION})")

if __name__ == "__main__":
    main()
