# Importa as bibliotecas pytest e requests
import pytest
import requests

# A fixture api_url() é uma função que retorna a URL base da API que será utilizada nos testes
# Essa função é uma maneira de fornecer dados ou recursos compartilhados entre os testes
@pytest.fixture
def api_url():
    return "https://swapi.dev/api/people/"

# Testa a consulta de uma pessoa existente na API
def test_get_pessoa_existente(api_url):
    # Faz uma requisição GET para a API para obter informações sobre a pessoa com ID 1
    response = requests.get(api_url + "1")
    # Verifica se o código de status da resposta é 200 (OK)
    assert response.status_code == 200
    # Verifica se a chave "name" está presente no JSON da resposta
    assert "name" in response.json()

# Testa a consulta de uma pessoa que não existe na API
def test_get_pessoa_nao_existente(api_url):
    # Faz uma requisição GET para a API para obter informações sobre uma pessoa com ID 999 (que não existe)
    response = requests.get(api_url + "999")
    # Verifica se o código de status da resposta é 404 (Not Found)
    assert response.status_code == 404

# Testa se a pessoa consultada possui uma espaçonave associada
def test_check_espaco_nave(api_url):
    # Faz uma requisição GET para a API para obter informações sobre a pessoa com ID 1
    response = requests.get(api_url + "1")
    # Verifica se o código de status da resposta é 200 (OK)
    assert response.status_code == 200
    # Verifica se a chave "starships" está presente no JSON da resposta
    assert "starships" in response.json()

# Testa como a API responde quando faltam parâmetros obrigatórios na requisição
def test_parametros_ausentes(api_url):
    # Faz uma requisição GET para a API sem fornecer parâmetros (intencionalmente)
    response = requests.get(api_url)
    # Verifica se o código de status da resposta é 400 (Bad Request)
    assert response.status_code == 400

# Testa diferentes métodos HTTP no mesmo endpoint
def test_diferentes_metodos_http(api_url):
    # Testa o método POST
    response_post = requests.post(api_url + "1")
    # Verifica se o código de status da resposta é 405 (Method Not Allowed)
    assert response_post.status_code == 405

    # Testa o método PUT
    response_put = requests.put(api_url + "1")
    # Verifica se o código de status da resposta é 405 (Method Not Allowed)
    assert response_put.status_code == 405

    # Testa o método DELETE
    response_delete = requests.delete(api_url + "1")
    # Verifica se o código de status da resposta é 405 (Method Not Allowed)
    assert response_delete.status_code == 405
