from flask import render_template, redirect, session, jsonify, request 
from app.routes import estudantes_bp
import uuid
from app.models import Estudante
from app import app, db

@estudantes_bp.route("/api/cadastrar-estudante", methods=["POST"])
def cadastrar_estudante():
    data = request.form 

    escolaridade = data.get("escolaridade")
    cursos = data.get("cursos")
    certificados = data.get("certificados")

    id = session["user_id"]

    new_estudante = Estudante(id=id, escolaridade=escolaridade, cursos=cursos, certificados=certificados)
    db.session.add(new_estudante)
    db.session.commit()

    return redirect("/pagina-inicial-estudante")



