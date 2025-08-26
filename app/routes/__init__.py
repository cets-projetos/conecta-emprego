from flask import Blueprint

users_bp = Blueprint('users', __name__)


from app.routes import users