from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello from inside a container!"

def test_health():
    client = app.test_client()
    assert client.get("/health").json["status"] == "ok"
