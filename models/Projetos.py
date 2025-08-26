from database import db

class Projeto (db.Model):
    id = db.Column (db.Integer, primary_key=True, nullable=False)
    nome = db.Column (db.String(50), nullable=False,)
    descricao = db.Column (db.String(200), nullable=False)
    tecnologias = db.Column (db.String(100), nullable=False)