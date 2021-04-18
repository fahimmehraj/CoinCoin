import graphene, json
import pymysql
import secrets
import random

from graphene.types import generic
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, request
from flask_graphql import GraphQLView
from schemas import GraphQL_user, GraphQL_offer
from flask_cors import CORS

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
CORS(app, origin="localhost:3000")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app) 


# model of user table from SQL database
class User(db.Model):
    userID = db.Column(db.String, primary_key=True, nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    display_name = db.Column(db.VARCHAR(25), unique=True, nullable=False)
    coin_val = db.Column(db.Integer)
    offers = db.relationship('Offer', backref=db.backref("user"))
    

# model of Offers table from SQL database
class Offer(db.Model):
    offerID = db.Column(db.String, primary_key=True)
    coinCoinOffer = db.Column(db.Integer)
    USDOffer = db.Column(db.Float)
    display_name = db.Column(db.VARCHAR(25))
    userID = db.Column(db.Integer)
    userID = db.Column(db.Integer, db.ForeignKey(User.userID), nullable=False)
    
    def __repr__(self):
        return "Offer ID {} created, {} coincoins for ${} ".format(offerID, coinCoinOffer, USDOffer)
# mutations
class CreateUser(graphene.Mutation):
    class Arguments:
        userID = graphene.String()
        email = graphene.String()
        displayName = graphene.String()
        coinVal = graphene.Int()
    ok = graphene.Boolean()
    user = graphene.Field(lambda: GraphQL_user)

    def mutate(self, info, userID, email, displayName, coinVal):
        user = GraphQL_user(
            userID=userID,
            email=email,
            displayName=displayName,
            coinVal=coinVal
        )
        DB_User = User(userID=userID, email=email, display_name=displayName, coin_val=coinVal)
        db.session.add(DB_User)
        db.session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)

class CreateOffer(graphene.Mutation):
    class Arguments:
        USDOffer = graphene.Float()
        coinOffer = graphene.Int()
        userID = graphene.String()
        displayName = graphene.String()
    ok = graphene.Boolean()
    offer = graphene.Field(lambda: GraphQL_offer)

    def mutate(self, info, USDOffer, coinOffer, userID, displayName):
        backOfferID = int("{}{}{}{}{}{}{}{}".format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)))

        offer = GraphQL_offer(
            offerID = backOfferID,
            USD_Offer = USDOffer,
            coin_Offer = coinOffer,
            userID = userID,
            displayName=displayName
        )
        DB_Offer = Offer(offerID=backOfferID, coinCoinOffer=coinOffer, USDOffer=USDOffer, userID=userID, display_name=displayName)
        db.session.add(DB_Offer)
        db.session.commit()
        ok = True
        return CreateOffer(offer=offer, ok=ok)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_offer = CreateOffer.Field()

# structure of query for graphql api
class Query(graphene.ObjectType):
    createUser = graphene.String(userID=graphene.String(), email=graphene.String(), displayName=graphene.String(), coinVal=graphene.Int())
    
    createOffer = graphene.String(userID=graphene.String(), coinOffer=graphene.Int(), USDOffer=graphene.Float())

    getUser= graphene.List(of_type=generic.GenericScalar, userID=graphene.String(default_value="none"), displayName=graphene.String(default_value=""))

    getOffer = graphene.List(of_type=generic.GenericScalar, offerID=graphene.Int(default_value=1), userID=graphene.String(default_value="none"))

    offers = graphene.List(of_type=generic.GenericScalar, offerID=graphene.Int(default_value=1), userID=graphene.String(default_value="none"))

    mineCoin=graphene.String(userID=graphene.String())

    # API rewrite methods
    getUserbyID = graphene.Field(GraphQL_user, userID=graphene.String(default_value="none"))

    getOfferbyID = graphene.Field(GraphQL_offer, offerID=graphene.Int(default_value=-1))

    mineCoinCoins = graphene.Field(GraphQL_user, userID=graphene.String(default_value="none"))

    transaction = graphene.Boolean(offerID=graphene.Int(), userID=graphene.String())

    cancelOffer = graphene.Boolean(offerID=graphene.Int())

    user = graphene.Field(GraphQL_user)

    offer = graphene.Field(GraphQL_offer)


        
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
    # deprecated
    def resolve_createUser(root, info, userID, email, displayName, coinVal):
        
        newUser_json = {    
            "userID": userID,
            "email": email,
            "displayName": displayName,
            "coinVal": coinVal
        }
        
        # adding new user to database
        newUser = User(userID=userID, email=email, display_name=displayName, coin_val=coinVal) 
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
    # deprecated
    def resolve_createOffer(root, info, userID, coinOffer, USDOffer):
        backOfferID = int("{}{}{}{}{}{}{}{}".format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)))

        dbOffer = Offer(offerID=backOfferID, coinCoinOffer=coinOffer, USDOffer=USDOffer, userID=userID)
        db.session.add(dbOffer)
        db.session.commit()

        return "Created offer {} by {}".format(backOfferID, userID)
    
    """
    getOffer method

    Fields
    ------
    offerID (optional) : int
        Searches database for offer using specified OfferID
    userID (optional): int
        Searches database for offers made by specified UserID
    
    Returns
    -------
    A list of offers
    """
    # deprecated
    def resolve_getOffer(self, info, offerID, userID):
        # if no offer ID is specified, search by user ID
        if offerID == 1:
            query_offer = Offer.query.filter_by(userID=userID)
            response = []
            for offer in query_offer:
                temp_dict = {
                    "offerID": offer.offerID,
                    "USD_Offer": offer.USDOffer,
                    "coin_Offer": offer.coinCoinOffer,
                    "userID": offer.userID
                }
                response.append(temp_dict)
            return response
        # if no user ID is specified, search by offer ID
        elif userID == "none":
            query_offer = Offer.query.filter_by(offerID=offerID)
            response = []
            for offer in query_offer:
                temp_dict = {
                    "OfferID": offer.offerID,
                    "USD_Offer": offer.USDOffer,
                    "coin_Offer": offer.coinCoinOffer,
                    "userID": offer.userID
                }
                response.append(temp_dict)
            return response

    """
    getUser method

    Fields
    ------
    userID (optional) : int
        Searches database based on specified user ID
    displayName (optional): str
        Searches database based on specified username/display name

    Returns
    ------
    A list of users containing information such as their ID, display name, email, and number of CoinCoins they have.

    """
    # deprecated, use resolve_getUserbyID instead
    def resolve_getUser(self, info, userID, displayName):
        # if no user ID is specified, search by display name
        if userID == "none":
            query_user = User.query.filter_by(display_name=displayName)
            response = []
            for user in query_user:
                temp_dict = {
                    "userID": user.userID,
                    "displayName": user.display_name,
                    "email": user.email,
                    "coinVal": user.coin_val
                }
                
                response.append(temp_dict)
            return response
        # if no display name is specified, search by user ID
        elif displayName == "":
            query_user = User.query.filter_by(userID=userID)
            response = []
            for user in query_user:
                temp_dict = {
                    "userID": user.userID,
                    "displayName": user.display_name,
                    "email": user.email,
                    "coinVal": user.coin_val
                }
                response.append(temp_dict)
            return response
    
    def resolve_offers(self, info, **args):
        all_offers = Offer.query.all()
        response = []
        for offer in all_offers:
            response.append({
                    "OfferID": offer.offerID,
                    "USD_Offer": offer.USDOffer,
                    "coin_Offer": offer.coinCoinOffer,
                    "userID": offer.userID
                })
        return response;

    # deprecated, use resolve_mineCoinCoins instead
    def resolve_mineCoin(self, info, userID):
        query_user = User.query.filter_by(userID=userID)[0]
        current_coinVal = query_user.coin_val
        query_user.coin_val = current_coinVal+1
        db.session.commit()
        return "User {} now has {} coincoins (previous was {}).".format(userID, current_coinVal+1, current_coinVal)
    

    # API Rewrite Methods
    def resolve_mineCoinCoins(self, info, userID):
        user = User.query.filter_by(userID=userID).first()
        newCoinVal = user.coin_val+1
        user.coin_val = newCoinVal
        db.session.commit()
        return GraphQL_user(
            userID=user.userID,
            displayName=user.display_name,
            email=user.email,
            coinVal=user.coin_val
        )        
    def resolve_transaction(self, info, offerID, userID):
        offer = Offer.query.filter_by(offerID=offerID).first()
        user = User.query.filter_by(userID=userID).first()
        coinCoins = offer.coinCoinOffer
        currentCoinVal = user.coin_val 
        user.coin_val = currentCoinVal+coinCoins
        db.session.delete(offer)
        db.session.commit()
        return True
    def resolve_cancelOffer(self, info, offerID):
        offer=Offer.query.filter_by(offerID=offerID).first()
        db.session.delete(offer)
        db.session.commit()
        return True


    def resolve_getOfferbyID(self, info, offerID):
        offer = Offer.query.filter_by(offerID=offerID).first()
        return GraphQL_offer(
            offerID=offer.offerID,
            USD_Offer=offer.USDOffer,
            coin_Offer=offer.coinCoinOffer,
            userID=offer.userID,
            displayName=offer.display_name
        )

    def resolve_getUserbyID(self, info, userID):
        user = User.query.filter_by(userID=userID).first()
        if user is not None:
            return GraphQL_user(
                userID=user.userID,
                displayName=user.display_name,
                email=user.email,
                coinVal=user.coin_val
            )
        else:
            return {}

schema = graphene.Schema(query=Query, mutation=Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))


if __name__ == '__main__':
    app.run(debug=True)


