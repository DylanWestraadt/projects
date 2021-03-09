from flask import Flask ,request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 

#init app
app = Flask(__name__)
#db base dir
base_dir = os.path.abspath(os.path.dirname(__file__))
#db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db init 
db = SQLAlchemy(app)
#marshmallow init
ma = Marshmallow(app)

#db model for products
class Product(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(150), unique=True)
    description = db.Column(db.String(300))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    #constructor to add our stuff to db 
    def __init__(self,name, description,price,qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty 

#Product Schema 
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True)

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']


    new_product = Product(name,description,price,qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

#server

if __name__ == "__main__":
    app.run("127.0.0.1", "4442" ,debug=True)
