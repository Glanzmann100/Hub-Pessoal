from app import db

class Usuario (db.Model):
    id = db.Collum (db.Integer, primary_key=True, nullable=False, auto_increment=True)
    nome = db.Collum (db.String(100), nullable=False )
    senha = db.Collum (db.String(50), nullable=False )