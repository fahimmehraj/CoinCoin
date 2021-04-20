import random

import graphene

from database import db
from schemas import GraphQL_user, GraphQL_offer
from tables import User, Offer

# Mutations
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
