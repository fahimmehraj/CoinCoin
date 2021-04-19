import graphene


class GraphQL_offer(graphene.ObjectType):
    offerID = graphene.Int()
    USD_Offer = graphene.Float()
    coin_Offer = graphene.Int()
    userID = graphene.String()
    displayName = graphene.String()


class GraphQL_user(graphene.ObjectType):
    userID = graphene.String()
    displayName = graphene.String()
    email = graphene.String()
    coinVal = graphene.Int()
    offers = graphene.List(of_type=GraphQL_offer)
