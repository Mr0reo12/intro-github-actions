from fastapi.testclient import TestClient
from main import app  # Asegúrate de que `main.py` esté en el mismo directorio raíz del proyecto

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "title": "My First API",
        "message": "Hello, Welcome to the API!"
    }

def test_get_usuarios():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert response.json() == {
        "usuarios": [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Jane Smith"},
            {"id": 3, "name": "Alice Johnson"},
            {"id": 4, "name": "Bob Brown"}
        ]
    }