#Import Flask
from flask import Flask, jsonify
#Create New Flask App Instance
app = Flask(__name__)
#Create First Route
@app.route('/')
def hello_world():
    return 'Hello world'

