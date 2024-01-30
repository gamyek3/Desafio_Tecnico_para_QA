# Caderno de Testes

## Teste de Consulta de Pessoas (GET /people)

### Consulta de Pessoa Existente

- **Parâmetros:** ID da pessoa existente (por exemplo, ID=1).
- **Resultados Esperados:** Status 200 e informações da pessoa.
- **Exemplo de Caso de Teste:** Testar com ID=1.

### Consulta de Pessoa Inexistente

- **Parâmetros:** ID de pessoa que não existe (por exemplo, ID=999).
- **Resultados Esperados:** Status 404 (Not Found).
- **Exemplo de Caso de Teste:** Testar com ID=999.

### Verificação de Espaço-Nave

- **Parâmetros:** ID de pessoa que existe (por exemplo, ID=1).
- **Resultados Esperados:** Status 200 e presença da chave "starships".
- **Exemplo de Caso de Teste:** Testar com ID=1.

### Teste com Falta de Parâmetros

- **Parâmetros:** Nenhum parâmetro.
- **Resultados Esperados:** Status 400 (Bad Request).
- **Exemplo de Caso de Teste:** Testar sem fornecer parâmetros.

### Teste de Métodos Diferentes no Endpoint

- Testar métodos POST, PUT, DELETE no endpoint /people.
- **Resultados Esperados:** Status 405 (Method Not Allowed).
- **Exemplo de Caso de Teste:** Testar cada método.

## Teste de Filmes (GET /films)

### Listagem quando há múltiplas pessoas cadastradas

- **Parâmetros:** Nenhum parâmetro.
- **Resultados Esperados:** Status 200 e presença da chave "results".
- **Exemplo de Caso de Teste:** Testar com dados existentes.

### Listagem quando não há pessoas cadastradas

- **Parâmetros:** Nenhum parâmetro.
- **Resultados Esperados:** Status 200 e lista vazia.
- **Exemplo de Caso de Teste:** Testar sem dados existentes.
