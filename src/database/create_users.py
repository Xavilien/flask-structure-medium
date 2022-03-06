"""
Insert dummy data into database
"""
from src import init_app
from src.models.models import User


def insert_dummy_data():
    app = init_app()
    with app.app_context():
        User.create('adam123', 'Adam', 'adam@gmail.com')


if __name__ == "__main__":
    insert_dummy_data()
