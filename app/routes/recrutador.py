from flask import render_template, redirect, session, jsonify, request, make_response, send_file
from app.routes import recrutador_bp
import uuid
from app.models import Recrutador
from app import app, db

@recrutador_bp.route("/api/cadastrar-recrutador", methods=["POST"])
def cadastrar_recrutador():
    data = request.form 

    empresa = data.get("empresa")
    cargo = data.get("cargo")
    descricao = data.get("descricao")

    id = session["user_id"]

    new_recrutador = Recrutador(id=id, empresa=empresa, cargo=cargo, descricao=descricao)
    db.session.add(new_recrutador)
    db.session.commit()

    return redirect("/pagina-inicial-recrutador")