import graphene 

class GraphQL_user(graphene.ObjectType):
    userID = graphene.String()
    displayName = graphene.String()
    email = graphene.String()
    coinVal = graphene.Int()
