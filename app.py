from flask import Flask 
from flask_restful import  Api 
from flask_jwt import JWT
from security import authenticate , identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # trun of flask's tracker not sqlaclchemy's
app.secret_key = "joe"

# going to authenticate
# it icreates a new end point , / auth , username and password
# send it to authenticate function
# if match return user
#


jwt = JWT(app,authenticate , identity)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()



api.add_resource(Item,'/item/<string:name>')  # student is now added to resources of API
api.add_resource(ItemList,'/items')  # ItemsList is now added to resources of API
api.add_resource(UserRegister,'/register')  # ItemsList is now added to resources of API

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000)

