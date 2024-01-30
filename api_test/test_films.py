# Importa as bibliotecas pytest e requests
import pytest
import requests

# A fixture films_api_url() é uma função que retorna a URL base da API de filmes que será utilizada nos testes
# Essa função é uma maneira de fornecer dados ou recursos compartilhados entre os testes
@pytest.fixture
def films_api_url():
    return "https://swapi.dev/api/films/"

# Testa a listagem de filmes quando há múltiplas pessoas cadastradas
def test_list_films_multiple_people(films_api_url):
    # Faz uma requisição GET para a API de filmes
    response = requests.get(films_api_url)
    # Verifica se o código de status da resposta é 200 (OK)
    assert response.status_code == 200
    # Verifica se a chave "results" está presente no JSON da resposta
    assert "results" in response.json()

# Testa a listagem de filmes quando não há pessoas cadastradas
def test_list_films_no_people(films_api_url):
    # Faz uma requisição GET para a API de filmes
    response = requests.get(films_api_url)
    # Verifica se o código de status da resposta é 200 (OK)
    assert response.status_code == 200
    # Considerando que não há pessoas cadastradas, verifica se a lista de filmes relacionados a pessoas é vazia
    assert len(response.json()["results"]) == 0
