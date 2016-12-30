import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
        os.environ['DB_PORT_27017_TCP_ADDR'],
        int(os.environ['MONGO_DB_PORT']))
db = client.testdb

@app.route('/')
def hello_world():
    connections_dict = db.command("serverStatus")["connections"]
    return connections_dict

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
