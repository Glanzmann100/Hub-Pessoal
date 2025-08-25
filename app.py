from flask import Flask, request, jsonify, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from routes.Login import usuarios_bp
from routes.Projetos import projetos_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Data.db"
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

#Blueprints das rotas
app.register_blueprint(usuarios_bp)
app.register_blueprint(projetos_bp)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)