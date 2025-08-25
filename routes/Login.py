from flask import Blueprint, request, jsonify,render_template
from models import Usuario
from app import db

usuarios_bp = Blueprint("usuarios", __name__)

#Rota de Listagem de Usuário
@usuarios_bp.route("/usuario", methods=["GET"])
def Usuarios():
    usuario = Usuario.query.all()
    return jsonify([{"id":u.id, "nome":u.nome, "senha":u.senha} for u in usuario])

#Rota de Cadastro de Usuário
@usuarios_bp.route("/Cadastro_Usuario", methods=["POST"])
def Cadastro_Usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    if senha != Usuarios:
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return jsonify({"mensagem": "usuário cadastrado com sucesso."}), 200

#Rota de Deletar Usuário
@usuarios_bp.route("/Deletar_Usuario/<int:id>", methods=["DELETE"])
def Deletar(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({"mensagem": "Usuário não encontrado no sistema."}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário deletado com sucesso."}), 200