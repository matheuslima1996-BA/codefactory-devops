"""
CodeFactory Solutions - Task Manager API
Aplicação de exemplo utilizada para demonstrar a adoção da Cultura DevOps.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# "Banco de dados" em memória apenas para fins de demonstração
tasks = [
    {"id": 1, "title": "Configurar ambiente de desenvolvimento", "done": True},
    {"id": 2, "title": "Padronizar versionamento com Git", "done": False},
]


@app.get("/")
def health_check():
    """Endpoint simples para verificar se a aplicação está no ar."""
    return jsonify({"status": "ok", "service": "task-manager-api"})


@app.get("/tasks")
def list_tasks():
    """Lista todas as tarefas cadastradas."""
    return jsonify(tasks)


@app.post("/tasks")
def create_task():
    """Cria uma nova tarefa."""
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    if not title:
        return jsonify({"error": "O campo 'title' é obrigatório"}), 400

    new_task = {
        "id": (tasks[-1]["id"] + 1) if tasks else 1,
        "title": title,
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.patch("/tasks/<int:task_id>/done")
def mark_task_done(task_id):
    """Marca uma tarefa como concluída."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)
    return jsonify({"error": "Tarefa não encontrada"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
