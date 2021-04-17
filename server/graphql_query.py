import graphene, json

class Query(graphene.ObjectType):
    createUser = graphene.String(id=graphene.ID(), email=graphene.String(), displayName=graphene.String(), coinVal=graphene.Int())
    data = graphene.String(name=graphene.String(), age=graphene.Int())
    
    def resolve_createUser(root, info, id, email, displayName, coinVal):
        newUser_json = {
            "id": id,
            "email": email,
            "displayName": displayName,
            "coinVal": coinVal
        }
        return newUser_json

    def resolve_data(root, info, name, age):
        return name, age
        