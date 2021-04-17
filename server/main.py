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
class Users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    display_name = db.Column(db.VARCHAR(25), nullable=False)
    coin_val = db.Column(db.Integer)
    # representation of data for testing


# model of Offers table from SQL database
class Offers(db.Model):
    offerID = db.Column(db.Integer, primary_key=True)
    coinCoinOffer = db.Column(db.Integer)
    USDOffer = db.Column(db.Float)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    
    def __repr__(self):
        return "Offer ID {} created, {} coincoins for ${} ".format(offerID, coinCoinOffer, USDOffer)
    


# structure of query for graphql api
class Query(graphene.ObjectType):
    createUser = graphene.String(email=graphene.String(), displayName=graphene.String(), coinVal=graphene.Int())

    getUser= graphene.String(userID=graphene.Int(default_value=2), displayName=graphene.String(default_value=""))
    
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
        all_ids = [x.userID for x in Users.query.all()]
        
        newUser_json = {    
            "userID": id,
            "email": email,
            "displayName": displayName,
            "coinVal": coinVal
        }
        
        # adding new user to database
        newUser = Users(userID=id, email=email, display_name=displayName, coin_val=coinVal)
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

        dbOffer = Offers(offerID=backOfferID, coinCoinOffer=coinOffer, USDOffer=USDOffer, userID=userID)
        db.session.add(dbOffer)
        db.session.commit()

        return "Created offer {} by {}".format(backOfferID, userID)
    
    def resolve_getUser(root, info, userID, displayName):
        # if no user ID is specified, search by display name
        if userID == 2:
            query_user = Users.query.filter_by(display_name=displayName)
            response = {}
            for user in query_user:
                print(user)
            return query_user.all()
        # if no display name is specified, search by user ID
        elif displayName == "":
            return displayName


schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=["GET", "POST"])
def graphql():
    data = json.loads(request.data)
    result = schema.execute(data['query'])
    return json.dumps(result.data)

if __name__ == '__main__':
    app.run(debug=True)
    
