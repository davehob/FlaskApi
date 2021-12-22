import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

# uri = os.getenv("DATABASE_URL")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# # rest of connection code using the connection string `uri`

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vkdlfdxdbyfsod:f6e6d3a75a2ca8ae5fee13dd2408b945e6ca9bcc0cfb1815e60edb6cdcfdbcdb@ec2-52-204-29-205.compute-1.amazonaws.com:5432/d8pnndod6kl51l'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
