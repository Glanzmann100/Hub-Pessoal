from flask import Blueprint, request, jsonify
from models import Evento
from database import db

eventos_bp = Blueprint("eventos", __name__)

# Rota de listagem de Eventos
@eventos_bp.route("/Lista_Eventos", methods=["GET"])
def Lista_Eventos():
    eventos = Evento.query.all()
    if not eventos:
        return jsonify({"mensagem": "Nenhum evento inserido"})
    return jsonify([{"id": e.id, "nome": e.nome, "descricao": e.descricao} for e in eventos])

# Rota de Inserção de Eventos 
@eventos_bp.route("/Cadastro_Eventos", methods=["POST"])
def Cadastrar_Eventos():
    data = request.get_json()
    id = data.get("id")
    nome = data.get("nome")
    descricao = data.get("descricao")
    novo_evento = Evento(id=id, nome=nome, descricao=descricao)
    db.session.add(novo_evento)
    db.session.commit()
    return jsonify({
        "mensagem": "Evento cadastrado com sucesso!",
        "Evento": {
            "id": novo_evento.id,
            "nome": novo_evento.nome,
            "descricao": novo_evento.descricao,
        }
    }), 201

# Rota de Deletar Eventos
@eventos_bp.route("/Deletar_Eventos/<int:id>", methods=["DELETE"])
def Deletar_Eventos(id):
    evento = Evento.query.get(id)
    if evento is None:
        return jsonify({"mensagem": "Evento não encontrado"}), 404
    db.session.delete(evento)
    db.session.commit()
    return jsonify({"mensagem": "Evento deletado com sucesso"}), 200