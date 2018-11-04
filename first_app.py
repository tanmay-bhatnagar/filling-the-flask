from flask import Flask

app = Flask(__name__)
# 
#POST 

@app.route('/') #http://www.google.com/'
def home():
    return "Hello"

Aapp.run(port = 5000)