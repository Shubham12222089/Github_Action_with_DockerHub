from app import app
def test_app():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
    assert b"Automated using CI/CD pipelines." in response.data