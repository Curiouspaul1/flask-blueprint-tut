from core import app
from models import db, users_schema, User
from flask import jsonify

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/getusers')
def getusers():
    users = User.query.all()
    return jsonify(users_schema.dump(users))
