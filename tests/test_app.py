import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.app import app  # noqa: E402


def test_health_check():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_list_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Nova tarefa de teste"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Nova tarefa de teste"


def test_create_task_without_title():
    client = app.test_client()
    response = client.post("/tasks", json={})
    assert response.status_code == 400
