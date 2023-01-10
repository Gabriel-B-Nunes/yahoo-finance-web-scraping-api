# API Yahoo Finance

## Objetivo do produto

O objetivo deste produto é ser uma API capaz de extrair os dados das empresas no website https://finance.yahoo.com/lookup e retornar um arquivo CSV.

## Backlog do produto

Como um user, eu gostaria de saber quais empresas estão listadas;
Como um user, eu gostaria de poder escolher qual empresa consultar;
Como um user, eu gostaria de consultar todas as empresas;

Como um user, eu gostaria de saber quais dados estão listados;
Como um user, eu gostaria de poder escolher quais dados da empresa extrair;
Como um user, eu gostaria de consultar todos os dados de todas as empresas.

### Objetivo do Sprint 1

Cria função que retorna as empresas listadas no site.

### Backlog do Sprint 1
1 conecta com o website usando requests;
2 transforma os dados em um objeto beautifulsoup;
3 localiza e armazena os nomes e simbolos das empresas;
4 retorna um arguivo csv OU imprimi na tela.