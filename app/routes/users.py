from flask import render_template, redirect, session, jsonify, request, make_response, send_file
from app.routes import users_bp 
import uuid 
from app.models import User
from app import app, db

@users_bp.route("/")
def homepage():
    return "Hello World"

@users_bp.route("/api/cadastrar-usuario", method=["POST"])
def cadastrar_usuario():
    data = request.form 

    username = data.get("username")
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    id = str(uuid.uuid4())

    new_user = User(id=id, username=username, nome=nome, senha=senha, email=email)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/pagina-inicial")

@users_bp.route("/api/login", methods=["POST"])
def login():
    data = request.form 

    username = data.get("username")
    senha = data.get("senha")

    user = User.query.filter_by(username=username, senha=senha).first()

    if user:
        session['user_id'] = user.id
        session.permanent = True
        return redirect("/pagina-inicial")
    else:
        return "Credenciais inválidas", 401

@users_bp.route("/api/logout")
def logout():
    session.pop('user_id', None)
    return redirect("/pagina-inicial")                                                  

