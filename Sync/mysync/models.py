from mysync import db

class Item(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, item):
        self.item = item

    def as_dict(self):
        return {'item': self.item}

class List(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64), index=True)
    listitem = db.Column(db.String(64), index=True)
    quantity = db.Column(db.String(64))

    def __init__(self, username, listitem, quantity):
        self.username = username
        self.listitem = listitem
        self.quantity = quantity

class User(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    userid = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, userid):
        self.userid = userid
