from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
    secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
CORS(app, origin="localhost:3000")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)
