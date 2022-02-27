from src import db


# User table
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email

    @staticmethod
    def create(username, name, email):
        """
        Create new user
        """
        new_user = User(username, name, email)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get_users():
        """
        :return: list of user details
        """
        users = [
            {
                'user_id': i.id,
                'username': i.username,
                'name': i.name,
                'email': i.email,
            }
            for i in User.query.order_by('id').all()
        ]
        return users
