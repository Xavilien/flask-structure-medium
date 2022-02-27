from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Databse setup
db = SQLAlchemy(app)
db.create_all()

from models import User


@app.route('/')
def index():
    users = User.get_users()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
