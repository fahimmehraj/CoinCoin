import graphene, json
import pymysql
import secrets

from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, request

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app) 


# model of user table from SQL database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    display_name = db.Column(db.VARCHAR(25), unique=True, nullable=False)
    coin_val = db.Column(db.Integer)
    # representation of data for testing
    def __repr__(self):
        return "successfully added user {}, named {}".format(id, display_name)

class Query(graphene.ObjectType):
    createUser = graphene.String(id=graphene.ID(), email=graphene.String(), displayName=graphene.String(), coinVal=graphene.Int())
    data = graphene.String(name=graphene.String(), age=graphene.Int())
    
    """
    createUser method

    Fields
    ------
    id : int
        Unique User ID number
    email : str
        User's email
    displayName : str
        The display name for the user
    coinVal : int
        The number of "CoinCoins" the user has

    """
    def resolve_createUser(root, info, id, email, displayName, coinVal):
        newUser_json = {
            "id": id,
            "email": email,
            "displayName": displayName,
            "coinVal": coinVal
        }
        newUser = Users(id=id, email=email, display_name=displayName, coin_val=coinVal)
        db.session.add(newUser)
        db.session.commit()
        return newUser_json

    def resolve_data(root, info, name, age):
        return name, age
        

schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=["GET", "POST"])
def graphql():
    data = json.loads(request.data)
    result = schema.execute(data['query'])
    if request.method == "GET":
        return "yes"
    if request.method == "POST":
        return json.dumps(result.data)

if __name__ == '__main__':
    app.run(debug=True)
    
