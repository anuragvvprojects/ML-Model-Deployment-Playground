from app.models.types import PredictRequest

def test_schema_model():
    p = PredictRequest(features=[1.0, 2.0, 3.0, 4.0], request_id="abc")
    assert p.features[0] == 1.0
    assert p.request_id == "abc"
