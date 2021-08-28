import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from resources.user import User
from resources.store import Store, StoreList
from resources.item import Item, ItemList
from security import authenticate, identity

app = Flask(__name__)

# create database
# ATTENTION - due to Heroku env variable has not
# update prefix 'postgres:' of the postgres URL, 
# have to replace the prefix with 'postgresql:'   
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.environ.get('DATABASE_URL', \
        'sqlite:///data.db').replace('postgres:', 'postgresql:')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.before_first_request
def create_all_table():
    db.create_all()  #create all tables before first call

# set up JWT authentication
app.secret_key = 'happy-toro-secret-key'
jwt = JWT(app=app, 
          authentication_handler=authenticate,
          identity_handler=identity)  # endpoint /auth

api = Api(app)
api.add_resource(User, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
