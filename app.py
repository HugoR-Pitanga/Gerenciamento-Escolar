from flask import Flask
from flask import request
from models import aluno, notas, token
from service import notas_service, aluno_service, token_service
import uuid
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/aluno')
def get_aluno():
    aluno_service_instance = aluno_service.AlunoService()
    alunos = aluno_service_instance.select()
    return json.dumps(alunos)

@app.route('/notas')
def get_notas():
    notas_service_instance = notas_service.NotaService()
    notas = notas_service_instance.select()
    return json.dumps(notas)

@app.route('/aluno', methods=['POST'])
def post_aluno():
    aluno_service_instance = aluno_service.AlunoService()
    data = request.get_json()
    print(data)
    nome = data['nome']
    aluno_instance = aluno.Aluno(None, nome)
    alunos = aluno_service_instance.create(aluno_instance)
    return str(alunos), 201

@app.route('/notas', methods=['POST'])
def post_notas():
    notas_service_instance = notas_service.NotaService()
    data = request.get_json()
    materia = data['materia']
    nota = data['nota']
    aluno_id = data['aluno_id']
    nota_instance = notas.Nota(None, materia, nota, aluno_id)
    notass = notas_service_instance.create(nota_instance)
    return str(notass)

@app.route('/token', methods=['POST'])
def post_token():
    token_tmp = uuid.uuid4()
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    data = request.get_json()
    token = f'{str(token_tmp)}{timestamp}'
    credential = {"user" : data['user'], "token" : token_tmp, "data_valida" : now }
    return token, 201

@app.route('/alunos/<id>', methods=['DELETE'])
def delete_aluno(id):
    aluno_service_instance = aluno_service.AlunoService()
    aluno_service_instance.delete_aluno(id)
    return "sucesso", 202