import graphene, json
import pymysql
import secrets 

from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, request

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app) 

# model of user table from SQL database
class DB_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    display_name = db.Column(db.VARCHAR(25), unique=True, nullable=False)
    coin_val = db.Column(db.Integer)

    # representation of data for testing
    def __repr__(self):
        return "id: {0} | email : {1}".format(self.id, self.email)


# structure of a query to graphql API
class Query(graphene.ObjectType):
    data = graphene.String(id=graphene.ID(), email=graphene.String(), displayName=graphene.String(), coinVal=graphene.Int())
    def resolve_data(root, info, id, email, displayName, coinVal):
        return id, email, displayName, coinVal
        
schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=["POST"])
def graphql():
    data = json.loads(request.data)
    result = schema.execute(data['query'])
    items = dict(result.data.items())
    return json.dumps(items)

if __name__ == '__main__':
    app.run(debug=True)
    
