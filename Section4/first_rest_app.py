from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
api = Api(app)
app.secret_key = 'tanmay'
 
jwt = JWT(app , authenticate , identity) #/auth (automatically generated
                                                 #   end point by JWT)
items = []
class Item(Resource):
    @jwt_required()
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
            return {'item' : None}  ,404
                
    def post(self,name):
        data = request.get_json()#(force = True) #Force = True DOES NOT CARE 
        #ABOUT THE HEADER IT JUST FORMATS IT TO THE APPROPRIATE FORMAT
        #silent = True displays nothing
        item = {'name' : name , 'price' : data['price']}
        items.append(item)
        return item, 201
    
class ItemList(Resource):
    def get(self):
        return {'items' : items}
    
    
api.add_resource(ItemList, '/items') 
api.add_resource(Item, '/item/<string:name>')
app.run(port=5000, debug = True)
