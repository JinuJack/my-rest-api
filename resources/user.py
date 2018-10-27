import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel
class UserResgister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank')
    def post(self):

        data = UserResgister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"A user that name already exists"},400

        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message":"user created successfully"},201



