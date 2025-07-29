def test_docs_openapi(client):
    assert client.get("/docs").status_code == 200
    assert client.get("/openapi.json").status_code == 200
