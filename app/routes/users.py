from flask import render_template, redirect, session, jsonify, request, make_response, send_file
from app.routes import users_bp 

@users_bp.route("/")
def homepage():
    return "Hello World"