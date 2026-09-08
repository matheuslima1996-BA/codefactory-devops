# Task Manager API — CodeFactory Solutions

## Descrição do projeto
Este repositório é a prova de conceito criada pela consultoria de adoção da
**Cultura DevOps** para a empresa fictícia **CodeFactory Solutions**. O objetivo
é demonstrar, na prática, como versionamento com Git/GitHub, containerização
com Docker e um pipeline de Integração Contínua resolvem os problemas de
padronização, colaboração e automação relatados pela empresa.

A aplicação de exemplo é uma **API REST de gerenciamento de tarefas**
(Task Manager API), construída em Python/Flask, escolhida por ser simples o
suficiente para não desviar o foco das práticas de DevOps, mas realista o
bastante para justificar testes automatizados, containerização e pipeline.

## Objetivo
- Demonstrar um fluxo de versionamento profissional (branches, pull requests,
  resolução de conflitos).
- Padronizar o ambiente de desenvolvimento com containers Docker.
- Automatizar build e testes por meio de um pipeline de Integração Contínua.
- Servir como modelo replicável para os demais projetos da equipe.

## Tecnologias utilizadas
- **Python 3.12** + **Flask** — API REST
- **Pytest** — testes automatizados
- **Flake8** — padronização/lint de código
- **Docker** e **Docker Compose** — containerização
- **Git** e **GitHub** — versionamento e colaboração
- **GitHub Actions** — pipeline de Integração Contínua

## Estrutura de pastas
```
codefactory-devops/
├── app/
│   └── app.py              # Código-fonte da API Flask
├── tests/
│   └── test_app.py         # Testes automatizados (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de Integração Contínua (GitHub Actions)
├── Dockerfile               # Receita da imagem da aplicação
├── docker-compose.yml       # Orquestração local (app + banco de dados)
├── requirements.txt         # Dependências Python
├── Jenkinsfile               # Pipeline alternativa (Jenkins)
├── .gitignore
├── LICENSE
└── README.md
```

## Instruções de instalação

### Opção 1 — Ambiente local
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Opção 2 — Docker (recomendado)
```bash
docker compose up --build
```

## Instruções de execução

### Rodando localmente
```bash
python app/app.py
# API disponível em http://localhost:5000
```

### Rodando os testes
```bash
pytest tests/ -v
```

### Rodando via Docker
```bash
docker compose up --build
# API disponível em http://localhost:5000
```

## Endpoints principais
| Método | Rota                     | Descrição                        |
|--------|--------------------------|-----------------------------------|
| GET    | `/`                      | Health check                      |
| GET    | `/tasks`                 | Lista todas as tarefas            |
| POST   | `/tasks`                 | Cria uma nova tarefa              |
| PATCH  | `/tasks/<id>/done`       | Marca uma tarefa como concluída   |
| GET    | `/tasks/<id>`            | Retorna uma tarefa específica     |

## Fluxo de branches
- `main` — código estável, pronto para produção.
- `desenvolvimento` — branch de integração das novas features.
- `features/*` — branches individuais para cada nova funcionalidade.

## Licença
Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE).

## Versão
`v1.0.0` — versão inicial da prova de conceito DevOps.
