
import sqlite3
from flask_restful import  Resource,reqparse
from flask_jwt import jwt_required
items = []
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
   
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field can not be blank"
    )
    
     
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="This field can not be blank"
    )
    
    def get(self,name):

        connecion = sqlite3.Connection('data.db')
        cursor = connecion.cursor()
        query = "Select * from items where name = ?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connecion.close()

        if row:
            return {'item':{'name':row[0],'price':row[1]} }
        return {'message':'item not found'}  ,404

    def post(self,name):
        #data = request.get_json()
        connecion = sqlite3.Connection('data.db')
        cursor = connecion.cursor()
        query = "Select * from items where name = ? "
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        
        if row:
            return {'message':'Item already exists'}  ,404
       
        data = Item.parser.parse_args()
        query = "Insert into items values(?,?,?)"
        cursor.execute(query,(name,data['price'],data['store_id']))

        connecion.commit()
        connecion.close() 

        return {'item':{'name':name,'price':data['price']} }


class ItemList(Resource):
    def get(self):
        return {"items": [ x.json() for x in ItemModel.query.all() ] }