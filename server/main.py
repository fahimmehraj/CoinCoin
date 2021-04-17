import graphene, json
import pymysql
import secrets
import random

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)




# model of user table from SQL database
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    display_name = db.Column(db.VARCHAR(25), unique=True, nullable=False)
    coin_val = db.Column(db.Integer)
    offers = db.relationship('Offer', backref=db.backref("user"))
    # representation of data for testing


# model of Offers table from SQL database
class Offer(db.Model):
    offerID = db.Column(db.Integer, primary_key=True)
    coinCoinOffer = db.Column(db.Integer)
    USDOffer = db.Column(db.Float)
    userID = db.Column(db.Integer, db.ForeignKey(User.userID), nullable=False)
    
    def __repr__(self):
        return "Offer ID {} created, {} coincoins for ${} ".format(offerID, coinCoinOffer, USDOffer)
    


# structure of query for graphql api
class Query(graphene.ObjectType):
    createUser = graphene.String(email=graphene.String(), displayName=graphene.String(), coinVal=graphene.Int())
    createOffer = graphene.String(userID=graphene.Int(), coinOffer=graphene.Int(), USDOffer=graphene.Float())
    
    """
    createUser method

    Fields
    ------
    email : str
        User's email
    displayName : str
        The display name for the user
    coinVal : int
        The number of "CoinCoins" the user has

    """
    def resolve_createUser(root, info, email, displayName, coinVal):
        id = int("{}{}{}{}{}{}{}{}".format(random.randint(0, 6), random.randint(0, 6), random.randint(0, 6), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)))

        
        newUser_json = {    
            "userID": id,
            "email": email,
            "displayName": displayName,
            "coinVal": coinVal
        }
        
        # adding new user to database
        newUser = User(userID=id, email=email, display_name=displayName, coin_val=coinVal)
        db.session.add(newUser)
        db.session.commit()
        return newUser_json

    """
    createOffer method

    Fields
    ------
    id : int
        Unique User ID number
    coinOffer : int
        The number of CoinCoins for USD
    USDOffer : int
        The number of USD for CoinCoins

    """

    def resolve_createOffer(root, info, userID, coinOffer, USDOffer):
        backOfferID = int("{}{}{}{}{}{}{}{}".format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)))

        dbOffer = Offer(offerID=backOfferID, coinCoinOffer=coinOffer, USDOffer=USDOffer, userID=userID)
        db.session.add(dbOffer)
        db.session.commit()

        return "Created offers"
        

schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=["GET", "POST"])
def graphql():
    for table in db.metadata.tables:
        print(str(table))
    data = json.loads(request.data)
    result = schema.execute(data['query'])
    if request.method == "GET":
        return "yes"
    if request.method == "POST":
        return json.dumps(result.data)

if __name__ == '__main__':
    app.run(debug=True)
    
