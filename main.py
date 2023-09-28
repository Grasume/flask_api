from flask import Flask
from flask import request
import docker
import os
import paramiko
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World !</h1>'

@app.route("/test")
def get_test_route():
    return "Test Route works"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)