from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

paciente = []

@app.route("/ficha/paciente", methods=['POST'])
def cadastro():
    entrada = request.json 
    for usuario in paciente:
        if usuario["id"] == entrada["id"]:  
            return {"Erro.":"ID ja cadastrado no sistema."}
    entrada = {
        "Nºficha": str(uuid.uuid4()),
        "id": entrada["id"],
        "senha": entrada["senha"]
        }
    paciente.append(entrada)
    return jsonify(entrada)

@app.route("/entrada/medica", methods=['POST'])
def logar():
    sistema = request.json
    for sistema in paciente:
        if sistema["id"] == sistema["id"] and sistema["senha"] == sistema["senha"]:
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