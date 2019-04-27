import sqlite3
from db import db

class StoreModel(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80))
    #back reference
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name ):
        self.name = name
        

    def json(self):
        return { 'name':self.name , 'items':[ x.json() for x in self.items.all() ] }
