import os
from os.path import join, dirname
from dotenv import load_dotenv 
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://hellen23:sparta@cluster0.p9rciek.mongodb.net/?retryWrites=true&w=majority')

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("mongodb+srv://hellen23:sparta@cluster0.p9rciek.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("dbsparta")

client = MongoClient(MONGODB_URI)
db = client.dbsparta

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)