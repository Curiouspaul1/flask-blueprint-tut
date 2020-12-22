from flask import Flask
import os

basedir = os.getcwd()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/dev.db"

import views
