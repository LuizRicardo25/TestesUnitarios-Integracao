# TestesUnitarios-Integracao
API REST Python Flask com Testes Unitários e de Integração

Este código é um exemplo de como escrever testes tanto unitários quanto de integração para uma aplicação Flask, utilizando a biblioteca `pytest` para estruturar e executar os testes. Vamos examinar cada parte detalhadamente.

### Importações

```python
import pytest
from app import app as flask_app
```

Aqui, estamos importando o `pytest`, que é uma framework de testes para Python. Também importamos a instância `app` do nosso aplicativo Flask do módulo `app`, renomeando-a como `flask_app` para evitar confusões com a fixture `app` que será definida mais adiante.

### Fixture `app`

```python
@pytest.fixture
def app():
    yield flask_app
```

Aqui, definimos uma fixture chamada `app` utilizando o decorador `@pytest.fixture`. Essa fixture simplesmente "yield" (produz) a instância do nosso aplicativo Flask (`flask_app`). O uso do `yield` permite a execução de código de limpeza após o teste, se necessário. Neste caso, é uma forma de disponibilizar a instância do Flask para outros testes ou fixtures.

### Fixture `client`

```python
@pytest.fixture
def client(app):
    return app.test_client()
```

A fixture `client` cria um cliente de teste utilizando a instância Flask gerada pela fixture `app`. O cliente de teste é um objeto especial fornecido pelo Flask que permite simular requisições HTTP ao aplicativo sem a necessidade de rodar o servidor. Isso é extremamente útil para testar as funcionalidades do aplicativo de maneira isolada.

### Teste Unitário `test_get_tasks`

```python
def test_get_tasks(client):
    """Teste unitário para a função get_tasks."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)
```

Este é um teste unitário para a função `get_tasks` do aplicativo Flask, que lista todas as tarefas. O teste utiliza o `client` para fazer uma requisição GET para a rota `/tasks` e verifica se:
- O código de status da resposta é 200, indicando sucesso.
- O corpo da resposta é uma instância de uma lista, conforme esperado pela funcionalidade da rota.

### Teste de Integração `test_add_task`

```python
def test_add_task(client):
    """Teste de integração para adicionar uma nova tarefa via POST."""
    task = {"id": 1, "title": "Study Flask"}
    response = client.post("/tasks", json=task)
    assert response.status_code == 201
    assert response.json == task

    # Verifica se a tarefa foi adicionada corretamente
    response = client.get("/tasks")
    assert task in response.json
```

Este é um teste de integração que verifica se uma nova tarefa pode ser adicionada corretamente via POST e, em seguida, se essa nova tarefa está presente quando listamos todas as tarefas. O teste:
- Envia uma requisição POST para `/tasks` com um objeto `task` como dados.
- Verifica se o código de status da resposta é 201, indicando que a tarefa foi criada com sucesso.
- Verifica se o objeto `task` retornado na resposta corresponde ao que foi enviado.
- Faz uma nova requisição GET para `/tasks` para verificar se a tarefa adicionada está presente na lista de tarefas.

### Conclusão

Esses testes são exemplos básicos de como você pode testar as funcionalidades de um aplicativo Flask. Testes unitários e de integração são essenciais para garantir que seu aplicativo esteja funcionando como esperado e para identificar regressões ou problemas potenciais rapidamente durante o desenvolvimento.