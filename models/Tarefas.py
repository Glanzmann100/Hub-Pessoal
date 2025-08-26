from database import db

class Tarefa (db.Model):
    id = db.Column (db.Integer, primary_key=True, nullable=False)
    nome = db.Column (db.String(100), nullable=False)
    descricao = db.Column (db.String(200), nullable=False)