from flask import Flask
from flask_restful import Api

from db import db
from resources.store import Store, StoreList
from resources.item import Item, ItemList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_all_table():
    db.create_all()  #create all tables before first call

api = Api(app)
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
