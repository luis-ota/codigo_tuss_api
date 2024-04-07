import json

import flask
import pandas as pd
from flask import Flask, jsonify, request

# Definir a largura máxima das colunas de exibição
pd.set_option('display.max_colwidth', None)

app = Flask(__name__)


@app.route('/cod_tuss/pesquisar/<string:termo>', methods=['GET', 'POST'])
def pesquisar_termo_por_texto(termo):
    # Carregar o arquivo CSV
    df = pd.read_csv('TUSS/Tabela_22_Procedimentos_e_eventos_em_saúde.csv', delimiter=';')

    # Filtrar o DataFrame pelo termo inserido
    df_filtrado = df[df['Termo'].str.contains(termo, case=False)]

    # Converter o DataFrame filtrado para JSON
    resultado_json = df_filtrado.to_json(orient='records')

    return resultado_json


@app.route('/cod_tuss/pesquisar/<int:cod_termo>', methods=['GET', 'POST'])
def pesquisar_termo_por_cod(cod_termo):
    # Carregar o arquivo CSV
    df = pd.read_csv('TUSS/Tabela_22_Procedimentos_e_eventos_em_saúde.csv', delimiter=';')

    # Converter a coluna 'Código do Termo' em uma string
    df['Código do Termo'] = df['Código do Termo'].astype(str)

    # Filtrar o DataFrame pelo termo inserido
    df_filtrado = df[df['Código do Termo'].str.contains(f'{cod_termo}', case=False)]

    # Converter o DataFrame filtrado para JSON
    resultado_json = df_filtrado.to_json(orient='records')

    return resultado_json

@app.route('/cod_tuss/pesquisar', methods=['GET'])
def pesquisar_e_paginar():
    args = request.args
    termo = args.get("filtroTermo", default="", type=str)
    cod_termo = args.get("filtroCodigo", default="", type=str)
    skipCount = args.get("skipCount", default=0, type=int)
    max_result_count = args.get("maxResultCount", default=5, type=int)

    # Carregar o arquiv CSV
    df = pd.read_csv('TUSS/Tabela_22_Procedimentos_e_eventos_em_saúde.csv', delimiter=';')

    # Filtrar o DataFrame pelo termo inserido
    df['Código do Termo'] = df['Código do Termo'].astype(str)
    df_filtrado = df

    if cod_termo and cod_termo != '':
        df_filtrado = df_filtrado[df_filtrado['Código do Termo'].str.contains(f'{cod_termo}', case=False)]

    if termo and termo != '':
        df_filtrado = df[df['Termo'].str.contains(termo, case=False)]

    # Converter o DataFrame filtrado para JSON
    totalCount = len(df_filtrado)
    resultado_json = df_filtrado.to_json(orient='records')

    items = json.loads(resultado_json)
    items = items[skipCount:]
    items = items[:max_result_count]

    resultado = {
        "totalCount": totalCount,
        "items": items,
    }

    return json.dumps(resultado)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
