from flask import Blueprint, request, jsonify, render_template
from models import Projeto
from database import db

projetos_bp = Blueprint("projetos", __name__)

#Rota de Listagem de Projetos
@projetos_bp.route("/Lista_Projetos", methods=["GET"])
def Lista_Projeto():
    projeto = Projeto.query.all()
    return jsonify([{"id":p.id, "nome":p.nome, "descricao":p.descricao, "tecnologias":p.tecnologias} for p in projeto])

#Rota de Adição de Projeto
@projetos_bp.route("/Cadastro_Projeto", methods=["POST"])
def Cadastro_Projeto():
    data = request.get_json()
    nome = data.get("nome")
    descricao = data.get("descricao")
    tecnologias = data.get("tecnologias")
    novo_projeto = Projeto(nome=nome, descricao=descricao, tecnologias=tecnologias)
    db.session.add(novo_projeto)
    db.session.commit()
    return jsonify({
        "mensagem": "Projeto cadastrado com sucesso!",
        "Projeto": {
            "id": novo_projeto.id,
            "nome": novo_projeto.nome,
            "descricao": novo_projeto.descricao,
            "tecnologias": novo_projeto.tecnologias
        }
    }), 201

#Rota de Deletar Projeto 
@projetos_bp.route("/Deletar_Projetos/<int:id>", methods=["DELETE"])
def Deletar_Projeto(id):
    projeto = Projeto.query.get(id)
    if not projeto:
        return jsonify({"mensagem": "Projeto não encontrado no sistema."}), 404
    db.session.delete(projeto)
    db.session.commit()
    return jsonify({"mensagem": "Projeto deletado com sucesso."}), 200