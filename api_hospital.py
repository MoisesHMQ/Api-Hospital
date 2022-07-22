from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

paciente = []

@app.route("/ficha/paciente", methods=['POST'])
def cadastro():
    entrada = request.json 
    for usuario in paciente:
        if usuario["nome"] == entrada["nome"]:  
            return {"Erro.":"paciente ja cadastrado no sistema."}
    entrada = {
        "nome": entrada["nome"],
        "Nºficha": str(uuid.uuid4()),
        "senha": entrada["senha"]
        }
    paciente.append(entrada)
    return jsonify(entrada)

@app.route("/entrada/paciente/sistema", methods=['POST'])
def logar():
    sistema = request.json
    for sistema in paciente:
        if sistema["Nºficha"] == sistema["Nºficha"] and sistema["senha"] == sistema["senha"]:
            return{"Status":"Login realizado."}
        else:
            return{"Erro.":"Dados do paciente inidaderetos."}

doença_sintomas = []

@app.route("/ficha/paciente", methods=['POST'])
def ficha_hospital():
    ficha = request.json
    for ficha in doença_sintomas:
        if ficha["cid"] == ficha["cid"]:
            return {"status": "Produto já cadastrado."}
    ficha = {
        "indentificação": str(uuid.uuid4()),
        "nome":ficha["nome"],
        "idade":ficha["idade"],
        "cid": ficha["cid"]
    }
    doença_sintomas.append(ficha)
    return jsonify(ficha)

@app.route("/pacientes/ativos")
def pacientes():
    return jsonify(paciente)

@app.route("/ficha/pacientes/ativos")
def ficha():
    return jsonify(doença_sintomas)



@app.route("/excluir/pacientes", methods=['POST'])
def excluir_pacientes():
    paciente_excluir = request.json
    print(paciente)
    for user in paciente:
        if user["Nºficha"] == paciente_excluir["Nºficha"]:
            paciente.remove(user)
            return paciente_excluir

@app.route("/excluir/fichas/ativas", methods=['POST'])
def excluir_fichas():
    ficha_excluir = request.json
    print(doença_sintomas)
    for list in doença_sintomas:
        if list["indentificação"] == ficha_excluir["indentificação"]:
            doença_sintomas.remove(list)
            return ficha_excluir



app.run()