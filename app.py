from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
import mongo

client = MongoClient(mongo.password, tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/j_page')
def j_home():
    return render_template('j_index.html')

@app.route('/h_page')
def h_home():
    return render_template('h_index.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
