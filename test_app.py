import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_tasks(client):
    """Teste unitário para a função get_tasks."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_task(client):
    """Teste de integração para adicionar uma nova tarefa via POST."""
    task = {"id": 1, "title": "Study Flask"}
    response = client.post("/tasks", json=task)
    assert response.status_code == 201
    assert response.json == task

    # Verifica se a tarefa foi adicionada corretamente
    response = client.get("/tasks")
    assert task in response.json