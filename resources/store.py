from flask_restful import Resource

from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        target_store = StoreModel.find_by_name(name)
        if target_store:
            return target_store.json()
        else:
            return ({'message': f'Store {name!r} does not exist'},
                    404)  # Http code - not found    

    def post(self, name):
        if StoreModel.find_by_name(name):
            return ({'message': f'Store {name!r} exists'}, 
                    401)  # Http code - bad request 

        new_store = StoreModel(name)
        new_store.save_to_db()
        return new_store.json(), 201  # Http code - created    

    def delete(self, name):
        target_store = StoreModel.find_by_name(name)
        if target_store:
            target_store.delete_from_db()
            return {'message': f'Store {name!r} is deleted'}
        else:
            return ({'message': f'Store {name!r} does not exist'},
                    404)  # Http code - not found    

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}    

