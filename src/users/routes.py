from flask import Blueprint, render_template
from src.models.user import User

bp = Blueprint('users', __name__)


@bp.route('/')
def index():
    users = User.get_users()
    return render_template('users.html', users=users)
