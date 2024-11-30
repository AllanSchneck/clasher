from os import EFD_SEMAPHORE
from flask import Flask, jsonify
import pandas as pd
from pandas.core.dtypes.dtypes import re
#Iniciar Flask
app = Flask(__name__)
#construir as funcionalidades


@app.route('/')
def homepage():
    return 'A API está no ar'


#basicamente essa função relata em que link irá rodar está página


@app.route('/contatos')
def contatos():
    return "Esse são os contatos"


@app.route('/principe')
def principe():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][0])
    raridade = str(tabela['Raridade'][0])
    carta = str(tabela['Carta'][0])
    elixir = str(tabela['Elixir'][0])
    alvo = str(tabela['Alvo'][0])
    alcance = str(tabela['Alcance'][0])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][0])
    valocidade = str(tabela['Velocidade'][0])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][0])
    quantidade = str(tabela['Quantidade'][0])
    movimentacao = str(tabela['Movimentacao'][0])
    tipo = str(tabela['Tipo'][0])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/mosqueteira')
def mosqueteira():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][1])
    raridade = str(tabela['Raridade'][1])
    carta = str(tabela['Carta'][1])
    elixir = str(tabela['Elixir'][1])
    alvo = str(tabela['Alvo'][1])
    alcance = str(tabela['Alcance'][1])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][1])
    valocidade = str(tabela['Velocidade'][1])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][1])
    quantidade = str(tabela['Quantidade'][1])
    movimentacao = str(tabela['Movimentacao'][1])
    tipo = str(tabela['Tipo'][1])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/minipekka')
def minipekka():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][2])
    raridade = str(tabela['Raridade'][2])
    carta = str(tabela['Carta'][2])
    elixir = str(tabela['Elixir'][2])
    alvo = str(tabela['Alvo'][2])
    alcance = str(tabela['Alcance'][2])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][2])
    valocidade = str(tabela['Velocidade'][2])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][2])
    quantidade = str(tabela['Quantidade'][2])
    movimentacao = str(tabela['Movimentacao'][2])
    tipo = str(tabela['Tipo'][2])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/bebedragao')
def bebe_dragao():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][3])
    raridade = str(tabela['Raridade'][3])
    carta = str(tabela['Carta'][3])
    elixir = str(tabela['Elixir'][3])
    alvo = str(tabela['Alvo'][3])
    alcance = str(tabela['Alcance'][3])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][3])
    valocidade = str(tabela['Velocidade'][3])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][3])
    quantidade = str(tabela['Quantidade'][3])
    movimentacao = str(tabela['Movimentacao'][3])
    tipo = str(tabela['Tipo'][3])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/cavaleiro')
def cavaleiro():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][4])
    raridade = str(tabela['Raridade'][4])
    carta = str(tabela['Carta'][4])
    elixir = str(tabela['Elixir'][4])
    alvo = str(tabela['Alvo'][4])
    alcance = str(tabela['Alcance'][4])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][4])
    valocidade = str(tabela['Velocidade'][4])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][4])
    quantidade = str(tabela['Quantidade'][4])
    movimentacao = str(tabela['Movimentacao'][4])
    tipo = str(tabela['Tipo'][4])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/arqueiras')
def arqueiras():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][5])
    raridade = str(tabela['Raridade'][5])
    carta = str(tabela['Carta'][5])
    elixir = str(tabela['Elixir'][5])
    alvo = str(tabela['Alvo'][5])
    alcance = str(tabela['Alcance'][5])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][5])
    valocidade = str(tabela['Velocidade'][5])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][5])
    quantidade = str(tabela['Quantidade'][5])
    movimentacao = str(tabela['Movimentacao'][5])
    tipo = str(tabela['Tipo'][5])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/gigante')
def gigante():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][6])
    raridade = str(tabela['Raridade'][6])
    carta = str(tabela['Carta'][6])
    elixir = str(tabela['Elixir'][6])
    alvo = str(tabela['Alvo'][6])
    alcance = str(tabela['Alcance'][6])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][6])
    valocidade = str(tabela['Velocidade'][6])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][6])
    quantidade = str(tabela['Quantidade'][6])
    movimentacao = str(tabela['Movimentacao'][6])
    tipo = str(tabela['Tipo'][6])

    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/magodegelo')
def mago_de_gelo():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][7])
    raridade = str(tabela['Raridade'][7])
    carta = str(tabela['Carta'][7])
    elixir = str(tabela['Elixir'][7])
    alvo = str(tabela['Alvo'][7])
    alcance = str(tabela['Alcance'][7])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][7])
    valocidade = str(tabela['Velocidade'][7])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][7])
    quantidade = str(tabela['Quantidade'][7])
    movimentacao = str(tabela['Movimentacao'][7])
    tipo = str(tabela['Tipo'][7])
    especial = str(tabela['Especial'][7])
    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo,
        'especial': especial
    }
    return jsonify(resposta)


@app.route('/bruxa')
def bruxa():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][8])
    raridade = str(tabela['Raridade'][8])
    carta = str(tabela['Carta'][8])
    elixir = str(tabela['Elixir'][8])
    alvo = str(tabela['Alvo'][8])
    alcance = str(tabela['Alcance'][8])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][8])
    valocidade = str(tabela['Velocidade'][8])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][8])
    quantidade = str(tabela['Quantidade'][8])
    movimentacao = str(tabela['Movimentacao'][8])
    tipo = str(tabela['Tipo'][8])
    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/bombardeiro')
def bombardeiro():
    tabela = pd.read_csv('cartas_tropa.csv')
    id = str(tabela['ID'][9])
    raridade = str(tabela['Raridade'][9])
    carta = str(tabela['Carta'][9])
    elixir = str(tabela['Elixir'][9])
    alvo = str(tabela['Alvo'][9])
    alcance = str(tabela['Alcance'][9])
    velocidade_do_impacto = str(tabela['Velocidade_do_impacto'][9])
    valocidade = str(tabela['Velocidade'][9])
    tempo_de_mobilizacao = str(tabela['Tempo_de_mobilizacao'][9])
    quantidade = str(tabela['Quantidade'][9])
    movimentacao = str(tabela['Movimentacao'][9])
    tipo = str(tabela['Tipo'][9])
    resposta = {
        'id': id,
        'carta': carta,
        'raridade': raridade,
        'elixir': elixir,
        'alvo': alvo,
        'alcance': alcance,
        'velocidade_do_impacto': velocidade_do_impacto,
        'velocidade': valocidade,
        'tempo_de_mobilizacao': tempo_de_mobilizacao,
        'quantidade': quantidade,
        'movimentacao': movimentacao,
        'tipo': tipo
    }
    return jsonify(resposta)


@app.route('/boladefogo')
def bola_de_fogo():
    tabela = pd.read_csv('cartas_feitico.csv')
    id = str(tabela['ID'][0])
    carta = str(tabela['Carta'][0])
    elixir = str(tabela['Elixir'][0])
    raio = str(tabela['Raio'][0])
    alvo = str(tabela['Alvo'][0])
    tipo = str(tabela['Tipo'][0])
    raridade = str(tabela['Raridade'][0])
    resposta = {
        'id': id,
        'carta': carta,
        'elixir': elixir,
        'raio': raio,
        'alvo': alvo,
        'tipo': tipo,
        'raridade': raridade,
    }
    return jsonify(resposta)


@app.route('/choque')
def choque():
    tabela = pd.read_csv('cartas_feitico.csv')
    id = str(tabela['ID'][1])
    carta = str(tabela['Carta'][1])
    elixir = str(tabela['Elixir'][1])
    raio = str(tabela['Raio'][1])
    alvo = str(tabela['Alvo'][1])
    tipo = str(tabela['Tipo'][1])
    raridade = str(tabela['Raridade'][1])
    resposta = {
        'id': id,
        'carta': carta,
        'elixir': elixir,
        'raio': raio,
        'alvo': alvo,
        'tipo': tipo,
        'raridade': raridade,
    }
    return jsonify(resposta)


app.run(host='0.0.0.0')

#caso vocÊ estiver rodando em replit você precisa dentro do parenteses do desta maneira "app.run(host='0.0.0.0')"
