from flask import Blueprint, request, jsonify
from models import Usuario
from database import db

usuarios_bp = Blueprint("usuarios", __name__)

# Rota de listagem de usuários
@usuarios_bp.route("/Lista_Usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nome": u.nome, "senha": u.senha} for u in usuarios])

# Rota de cadastro de usuário
@usuarios_bp.route("/Cadastro_Usuarios", methods=["POST"])
def cadastrar_usuario():
    data = request.get_json()
    id = data.get("id")
    nome = data.get("nome")
    senha = data.get("senha")
    novo_usuario = Usuario(id=id, nome=nome, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!",
        "usuario": {
            "id": novo_usuario.id,
            "nome": novo_usuario.nome,
            "senha": novo_usuario.senha,
        }
    }), 201

# Rota de deletar usuário
@usuarios_bp.route("/Deletar_Usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado no sistema."}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário deletado com sucesso."}), 200