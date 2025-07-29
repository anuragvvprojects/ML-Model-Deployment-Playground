def test_predict_contract(client):
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert set(body.keys()) >= {"prediction", "proba", "model_version"}
    assert isinstance(body["prediction"], int)
    assert 0.0 <= body["proba"] <= 1.0
