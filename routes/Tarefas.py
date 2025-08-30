from flask import Blueprint, request, jsonify
from models import Tarefa
from database import db

tarefas_bp = Blueprint("tarefas", __name__)


#Rota de Listagem de Tarefas
@tarefas_bp.route("/Lista_Tarefas", methods=["GET"])
def Listagem_Tarefas():
    tarefa = Tarefa.query.all()
    return jsonify([{"id": t.id, "nome": t.nome, "descricao": t.descricao} for t in tarefa])

#Rota de Adição de Tarefa
@tarefas_bp.route("/Adicionar_Tarefa", methods=["POST"])
def Adicionar_Tarefa():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    nova_tarefa = Tarefa(nome=nome, descricao=descricao)
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({"mensagem": "Tarefa cadastrada com sucesso!"})

#Rota de Deletar Tarefa
@tarefas_bp.route("/Deletar_Tarefa/<int:id>", methods=["DELETE"])
def Deletar_Tarefa(id):
    tarefa = Tarefa.query.get(id)
    if tarefa is None:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({"mensagem": "Tarefa deletada com sucesso"}), 200