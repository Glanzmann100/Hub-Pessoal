from flask import Flask
from flask import request, jsonify, redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://Data.db"
db = SQLALchemy(app)
