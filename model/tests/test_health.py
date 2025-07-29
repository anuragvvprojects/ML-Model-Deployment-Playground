def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_ready(client):
    r = client.get("/ready")
    assert r.status_code == 200
    assert "ready" in r.json()
