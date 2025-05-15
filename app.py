from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/",methods = ['GET'])
def home():
    return "Welcome to the FUll Stack Development"

@app.route("/greet",methods = ['POST'])
def greet():
    data = request.json
    name = data.get('name','Guest')
    return jsonify({'message':f'Hello,{name}!Welcome from Flask API'})

if __name__ == '__main__':
    app.run(debug=True)