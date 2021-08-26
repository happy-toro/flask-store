from flask_restful import Resource, reqparse

from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
                        type=str,
                        required=True, 
                        help='Username is required')
    parser.add_argument('password', 
                        type=str,
                        required=True, 
                        help='password is required')

    def post(self):
        data = self.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return ({'message': 
                    f'Username {data["username"]!r} is used'},
                    401)  # Http code - bad request 

        new_user = UserModel(**data)
        new_user.save_to_db()
        return ({'message': 
                f'Username {data["username"]!r} is created'},
                201)  # Http code - created 
