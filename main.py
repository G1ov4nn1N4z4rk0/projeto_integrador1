# API -> E um lugar para disponibilizar recursos e/ou funcionalidades. UMA PONTE
# 1. Objetivos - Criar uma API que disponibiliza a consulta, criacao, edicao e exclusao de carros
# 2 URL base - localhost
# 3 Endpoints -
        # localhost/carros(GET)
        # localhost/carros(PUT)
        # localhost/carros(DELET)
        # localhost/carros id (GET)


from flask import Flask,jsonify, make_response, request # type: ignore
# Importa o banco de dados
from bd import Carros

# Instanciar o modulo Flask na nossa variavel app
app = Flask('carros')

# PRIMEIRO METODO - VISUALIZAR OS DADOS (GET)
# app.route -> definir que essa funcao e uma rota que o flask entenda que aquilo e um metodo que deve ser executado
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

# PRIMEIRO METODO PARTE 2 - VISUALIZAR DADOS POR ID (GET / ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for cada_carro in Carros:
        if cada_carro.get('id') == id:
            return jsonify(cada_carro)

# SEGUNDO METODO - CRIAR NOVOS DADOS (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso',
                carro=carro)
    )


# TERCEIRO METODO - EDITAR DADOS (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])

# QUARTO METODO - DELETAR DADOS (DELETE)
@app.route('/carros/<int:id>',methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem:":"carro excluido com sucesso"})


app.run(port=5000, host='localhost')