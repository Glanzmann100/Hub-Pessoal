from flask import Flask
from database import db
from routes.Registro import usuarios_bp
from routes.Projetos import projetos_bp
from routes.Calendario import eventos_bp
from routes.Tarefas import tarefas_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Data.db"

db.init_app(app)

with app.app_context():
    db.create_all()

# registrar blueprints
app.register_blueprint(usuarios_bp)
app.register_blueprint(projetos_bp)
app.register_blueprint(eventos_bp)
app.register_blueprint(tarefas_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)