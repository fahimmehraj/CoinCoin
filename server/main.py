import graphene
from flask_graphql import GraphQLView

from database import app
from query import Query
from mutations import Mutations

schema = graphene.Schema(query=Query, mutation=Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))


if __name__ == '__main__':
    app.run(debug=True)
