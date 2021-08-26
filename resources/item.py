from flask_restful import Resource, reqparse

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
                        type=float, 
                        required=True, 
                        help='Must spell the price for the item')
    parser.add_argument('store_id', 
                        type=int, 
                        required=True, 
                        help='Must spell the id of the store that this item belongs to')

    def get(self, name):
        target_item = ItemModel.find_by_name(name)
        if target_item:
            return target_item.json()
        else:
            return ({'message': f'Item {name!r} does not exist'},
                    404)  # Http code - not found

    def post(self, name):
        if ItemModel.find_by_name(name):
            return ({'message': f'Item {name!r} exists'},
                    401)  # Http code - bad request

        data = self.parser.parse_args()
        new_item = ItemModel(name, **data)
        new_item.save_to_db()
        return new_item.json(), 201  # Http code - created

    def put(self, name):
        data = self.parser.parse_args()
        target_item = ItemModel.find_by_name(name)
        if target_item:
            target_item.price = data['price']
            target_item.store_id = data['store_id']
            target_item.save_to_db()
            return target_item.json()
        else:
            new_item = ItemModel(name, **data)
            new_item.save_to_db()
            return new_item.json(), 201  # Http code - created    

    def delete(self, name):
        target_item = ItemModel.find_by_name(name)
        if target_item:
            target_item.delete_from_db()
            return {'message': f'Item {name!r} is deleted'}
        else:
            return ({'message': f'Item {name!r} does not exist'},
                    404)  # Http code - not found


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}