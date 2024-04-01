import pandas as pd
from flask import Flask, jsonify

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
