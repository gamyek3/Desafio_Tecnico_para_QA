# Caderno de Testes

## Teste de Consulta de Pessoas (GET /people)

### Consulta de Pessoa Existente

Dado que eu tenho uma pessoa com o ID 1
Quando eu faço uma consulta para obter detalhes da pessoa
Então eu devo receber um status de resposta 200
E eu devo ver informações válidas da pessoa

### Consulta de Pessoa Inexistente

Dado que eu tenho uma pessoa com o ID 999 que não existe
Quando eu faço uma consulta para obter detalhes da pessoa
Então eu devo receber um status de resposta 404

### Verificação de Espaço-Nave

Dado que eu tenho uma pessoa com o ID 1
Quando eu faço uma consulta para obter detalhes da pessoa
Então eu devo receber um status de resposta 200
E eu devo ver informações sobre a espaçonave associada à pessoa

### Teste com Falta de Parâmetros

Dado que eu não forneço parâmetros na consulta
Quando eu faço uma consulta para obter detalhes da pessoa
Então eu devo receber um status de resposta 400

### Teste de Métodos Diferentes no Endpoint

Dado que eu faço uma consulta usando um método diferente de GET
Quando eu faço uma consulta para obter detalhes da pessoa
Então eu devo receber um status de resposta 405

## Teste de Filmes (GET /films)

### Listagem quando há múltiplas pessoas cadastradas

Dado que eu tenho várias pessoas cadastradas
Quando eu faço uma consulta para obter a lista de filmes
Então eu devo receber um status de resposta 200
E eu devo ver uma lista de filmes válida

### Listagem quando não há pessoas cadastradas

Dado que eu não tenho pessoas cadastradas
Quando eu faço uma consulta para obter a lista de filmes
Então eu devo receber um status de resposta 200
E eu devo ver uma lista vazia de filmes
