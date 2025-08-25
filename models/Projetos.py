from app import db

class Projeto (db.Model):
    id = db.Collum (db.Integer, primary_key=True, nullable=False, auto_increment=True)
    nome = db.Collum (db.String(50), nullable=False,)
    descricao = db.Collum(db.String(200), nullable=False)
    tecnologias = db.Collum(db.String(100), nullable=False)