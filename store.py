from flask import Flask, jsonify

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
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

#POST /store/<string:name>/item {name: , price}
@app.route('/store/<string:name>/item' , methods = ['POST'])
def create_item_in_store():
    pass

#GET /store/<string::name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run(port = 4000)
