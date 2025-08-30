from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_bp = Blueprint("usuarios", __name__)

# Rota de listagem de usuários
@usuarios_bp.route("/Lista_Usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nome": u.nome, "senha": u.senha, "email": u.email} for u in usuarios])

# Rota de cadastro de usuário
@usuarios_bp.route("/Cadastro_Usuarios", methods=["POST"])
def Cadastrar_Usuario():
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    email = request.form.get("email")
    novo_usuario = Usuario(nome=nome, senha=senha, email=email)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"})

# Rota de deletar usuário
@usuarios_bp.route("/Deletar_Usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado no sistema."}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário deletado com sucesso."}), 200