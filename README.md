# API Yahoo Finance

## Objetivo do produto

O objetivo deste produto é ser uma API capaz de extrair os dados das empresas no website https://finance.yahoo.com/lookup e retornar um arquivo CSV.

## Backlog do produto

* Como um user, eu gostaria de saber quais empresas estão listadas;
* Como um user, eu gostaria de poder escolher qual empresa consultar;
* Como um user, eu gostaria de consultar todas as empresas;
* Como um user, eu gostaria de consultar todos os dados de todas as empresas.

### Objetivo do Sprint 1

Cria função que retorna as empresas listadas no site.

### Backlog do Sprint 1
1. conecta com o website usando requests;
2. transforma os dados em um objeto beautifulsoup;
3. localiza e armazena os nomes e simbolos das empresas;
4. retorna simbolos, nomes ou ambos.

### Objetivo do Sprint 2

Cria função que consulta uma empresa específicada por simbolo

### Backlog do Sprint 2
1. conecta com o website usando requests e o simbolo da empresa;
2. transforma os dados em um objeto beautifulsoup;
3. localiza e armazena as legendas e valores;
4. retorna os valores OU cria arquivo csv.

### Objetivo do Sprint 3

Cria função que consulta todas as empresas e retorna os valores OU cria arquivo csv.

### Backlog do Sprint 3
1. usa a função lista_empresas para obter todos os simbolos;
2. usa a função pesquisa em loop para cada simbolo em simbolos;
3. retorna todos os resultados em um dicionário OU cria arquivo csv.
