# API de Pesquisa de Códigos TUSS

Esta é uma API simples desenvolvida em Python usando Flask para pesquisar códigos e termos da Tabela de Procedimentos e Eventos em Saúde (TUSS) fornecida em um arquivo CSV. A API oferece duas rotas para pesquisar os termos com base no texto ou no código.

## Como Usar

1. **Instalação de Dependências**: Primeiro, certifique-se de ter todas as dependências instaladas. Você pode instalá-las executando o seguinte comando:

   ```
   pip install pandas flask
   ```

2. **Executar a Aplicação**: Para iniciar a API, execute o seguinte comando:

   ```
   python main.py
   ```

3. **Enviar Requisições**: Você pode enviar solicitações HTTP GET ou POST para as rotas fornecidas para pesquisar termos por texto ou código TUSS.

   Exemplo de solicitação GET utilizando `curl` para pesquisar um termo por texto:
   ```
   curl http://localhost:105/cod_tuss/pesquisar/termo_a_pesquisar
   ```

   Exemplo de solicitação GET utilizando `curl` para pesquisar um termo por código:
   ```
   curl http://localhost:105/cod_tuss/pesquisar/1234
   ```

## Rotas

- `/cod_tuss/pesquisar/<string:termo>`
  - **Métodos Permitidos**: GET, POST
  - **Descrição**: Esta rota permite pesquisar termos por texto na Tabela TUSS.
  - **Parâmetros**:
    - `<string:termo>`: O termo a ser pesquisado na Tabela TUSS.
  - **Resposta**: Retorna um JSON contendo os termos que correspondem à pesquisa.

- `/cod_tuss/pesquisar/<int:cod_termo>`
  - **Métodos Permitidos**: GET, POST
  - **Descrição**: Esta rota permite pesquisar termos por código TUSS na Tabela TUSS.
  - **Parâmetros**:
    - `<int:cod_termo>`: O código TUSS a ser pesquisado na Tabela TUSS.
  - **Resposta**: Retorna um JSON contendo os termos que correspondem à pesquisa.

## Notas

- Certifique-se de ter o arquivo CSV da Tabela TUSS (`Tabela_22_Procedimentos_e_eventos_em_saúde.csv`) no diretório TUSS no mesmo diretório que o arquivo Python que contém este código.
- Esta API é destinada apenas para fins educacionais e pode exigir ajustes adicionais para uso em produção, como tratamento de erros, autenticação e autorização.
