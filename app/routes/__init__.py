from flask import Blueprint

users_bp = Blueprint('users', __name__)
estudantes_bp = Blueprint('estudantes', __name__)   
recrutador_bp = Blueprint('recrutador', __name__)

from app.routes import users, estudantes, recrutador 