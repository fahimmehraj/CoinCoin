import graphene
import secrets
import random

from graphene.types import generic
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_graphql import GraphQLView
from schemas import GraphQL_user, GraphQL_offer
from flask_cors import CORS

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
    secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

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
        return "Offer ID {} created, {} coincoins for ${} ".format(self.offerID, self.coinCoinOffer, self.USDOffer)

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
            coinVal=coinVal,
            offers=[]
        )
        DB_User = User(userID=userID, email=email,
                       display_name=displayName, coin_val=coinVal)
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
        backOfferID = int("{}{}{}{}{}{}{}{}".format(random.randint(0, 9), random.randint(0, 9), random.randint(
            0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)))

        offer = GraphQL_offer(
            offerID=backOfferID,
            USD_Offer=USDOffer,
            coin_Offer=coinOffer,
            userID=userID,
            displayName=displayName
        )
        DB_Offer = Offer(offerID=backOfferID, coinCoinOffer=coinOffer,
                         USDOffer=USDOffer, userID=userID, display_name=displayName)
        db.session.add(DB_Offer)
        db.session.commit()
        ok = True
        return CreateOffer(offer=offer, ok=ok)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_offer = CreateOffer.Field()

# structure of query for graphql api


class Query(graphene.ObjectType):
    offers = graphene.List(of_type=GraphQL_offer)

    users = graphene.List(of_type=GraphQL_user)

    # API rewrite methods
    user = graphene.Field(
        GraphQL_user, userID=graphene.String(default_value="none"))

    offer = graphene.Field(
        GraphQL_offer, offerID=graphene.Int(default_value=-1))

    mineCoinCoins = graphene.Field(
        GraphQL_user, userID=graphene.String(default_value="none"))

    transaction = graphene.Boolean(
        offerID=graphene.Int(), userID=graphene.String())

    cancelOffer = graphene.Boolean(offerID=graphene.Int())

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
        offer = Offer.query.filter_by(offerID=offerID).first()
        db.session.delete(offer)
        db.session.commit()
        return True

    def resolve_offer(self, info, offerID):
        offer = Offer.query.filter_by(offerID=offerID).first()
        return GraphQL_offer(
            offerID=offer.offerID,
            USD_Offer=offer.USDOffer,
            coin_Offer=offer.coinCoinOffer,
            userID=offer.userID,
            displayName=offer.display_name
        )

    def resolve_offers(self, info):
        offers_query = Offer.query.all()
        if offers_query is not None:
            offers = [GraphQL_offer(
                offerID=offer.offerID,
                USD_Offer=offer.USDOffer,
                coin_Offer=offer.coinCoinOffer,
                userID=offer.userID,
                displayName=offer.display_name
            ) for offer in offers_query]
        else:
            offers = []
        return offers

    def resolve_user(self, info, userID):
        user = User.query.filter_by(userID=userID).first()
        if user is not None:
            offers_query = Offer.query.filter_by(userID=userID).all()
            if offers_query is not None:
                offers = [GraphQL_offer(
                    offerID=offer.offerID,
                    USD_Offer=offer.USDOffer,
                    coin_Offer=offer.coinCoinOffer,
                    userID=offer.userID,
                    displayName=offer.display_name
                ) for offer in offers_query]
            else:
                offers = []
            return GraphQL_user(
                userID=user.userID,
                displayName=user.display_name,
                email=user.email,
                coinVal=user.coin_val,
                offers=offers
            )
        else:
            return {}
    
    # i am so proud of this function like im a genius
    def resolve_users(self, info):
        users_query = db.session.query(User, Offer).outerjoin(Offer).all()
        if users_query is not None:
            users = [GraphQL_user(
                userID=join[0].userID,
                displayName=join[0].display_name,
                email=join[0].email,
                coinVal=join[0].coin_val,
                offers=[GraphQL_offer(
                    offerID=offer.offerID,
                    USD_Offer=offer.USDOffer,
                    coin_Offer=offer.coinCoinOffer,
                    userID=offer.userID,
                    displayName=offer.display_name
                ) for offer in join if type(offer) is Offer]
            ) for join in users_query]
        else:
            users = []
        return users


schema = graphene.Schema(query=Query, mutation=Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))


if __name__ == '__main__':
    app.run(debug=True)
