import os
def is_enabled(flag: str) -> bool:
    return os.getenv(f"FLAG_{flag.upper()}", "false").lower() in ("1","true","yes","on")
    
    
class ModelService:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self._model = None
        self._version = "unknown"

    def load(self) -> None:
        artifact = joblib.load(self.model_path)
        self._model = artifact["model"]
        self._version = artifact.get("version", "unknown")

    def predict(self, features) -> Tuple[int, float]:
        import numpy as np
        X = np.array(features, dtype=float).reshape(1, -1)
        proba_arr = self._model.predict_proba(X)[0]
        pred = int(proba_arr.argmax())
        proba = float(proba_arr[pred])
        return pred, proba

    @property
    def ready(self) -> bool:
        return self._model is not None

    @property
    def version(self) -> str:
        return self._version

