from flask import Blueprint, request, jsonify,render_template
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
    if not nome or not descricao:
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400
    nova_tarefa = Tarefa(nome=nome, descricao=descricao)
    db.session.add(nova_tarefa)
    db.session.commit()
    tarefas = Tarefa.query.all()
    return render_template("Lista-Tarefas.html", tarefas=tarefas)

#Rota de Deletar Tarefa
@tarefas_bp.route("/Deletar_Tarefa/<int:id>", methods=["DELETE"])
def Deletar_Tarefa(id):
    tarefa = Tarefa.query.get(id)
    if tarefa is None:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({"mensagem": "Tarefa deletada com sucesso"}), 200