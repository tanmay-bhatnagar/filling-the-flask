from flask import Flask, jsonify, request

#POST - used to recieve data
#GET - used to send data 
#The above is true for programmer or user, reverse is true for browser
app = Flask(__name__)


stores = [
        {
                'name' : 'Store1',
                'items': [                        
                        {
                        'name' : 'My Item',
                        'price' : 420
                        }       
                        
                        ]
                
        }
        
        
]
#POST /store data : {name:}
@app.route('/store' , methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
            'name' : request_data['name'],
            'items' : []
            }
    stores.append(new_store)
    return jsonify(new_store)
    
#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return(jsonify({'message' : 'store not found'}))

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass


#GET /store/<string::name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items' : store['items']})
    return jsonify({'message' : 'store not found'})
    
    
app.run(port = 4000)
