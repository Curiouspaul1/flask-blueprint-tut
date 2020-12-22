from core import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# sqlalchemy instance
db = SQLAlchemy(app)
ma = Marshmallow(app)


# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(80))
    password = db.Column(db.String(50))


# JSON Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

if __name__ == "__main__":
    db.create_all()
    user1 = User(
        name="Paul John",email="pj@gmail.com",
        password="pjmaxson2020#"
    )
    user2 = User(
        name="John Doe",email="JD@gmail.com",
        password="jdmaxson2020#"
    )
    db.session.add_all([user1,user2])
    db.session.commit()