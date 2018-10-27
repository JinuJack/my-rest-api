from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from Rest_SqlAlchemy.resources.item import Item, ItemList
from Rest_SqlAlchemy.resources.user import UserResgister
from security import authentication, identity
from resources.store import Store,StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

app.secret_key = "shailu"

jwt = JWT(app,authentication,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserResgister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)