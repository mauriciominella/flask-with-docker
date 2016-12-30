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
    buildinfo = db.command("buildinfo")
    # return connections_dict
    print(buildinfo['version'])
    return 'Flash with mongo :D'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
