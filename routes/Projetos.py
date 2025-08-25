from flask import Blueprint, request, jsonify, render_template
from models import Projeto
from app import db

projetos_bp = Blueprint("projetos", __name__)

#Rota de Listagem de Projetos
@projetos_bp.route("/Projetos", methods=["GET"])
def Lista_Projeto():
    projetos = Projeto.query.all()
    return jsonify([{"id":p.id, "nome":p.nome, "descricao":p.descricao, "tecnologias":p.tecnologias} for p in projetos])

#Rota de Adição de Projeto
@projetos_bp.route("/Cadastro_Projeto", methods=["POST"])
def Cadastro_Projeto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    tecnologias = request.form["tecnologias"]
    novo_projeto = Projeto(id=id, nome=nome, descricao=descricao, tecnologias=tecnologias)
    db.session.add(novo_projeto)
    db.session.commit()

#Rota de Deletar Projeto 
@projetos_bp.route("/Deletar_Projeto/<int:id>", methods=["DELETE"])
def deletar_projeto(id):
    projeto = Projeto.query.get(id)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado."}), 404
    db.session.delete(projeto)
    db.session.commit()
    return jsonify({"mensagem": "Projeto deletado com sucesso."}), 200