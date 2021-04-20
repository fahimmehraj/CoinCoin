import graphene

from database import db
from schemas import GraphQL_user, GraphQL_offer
from tables import User, Offer

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
