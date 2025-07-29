def test_version(client):
    r = client.get("/version")
    assert r.status_code == 200
    body = r.json()
    assert "service_version" in body
    assert "model_version" in body
