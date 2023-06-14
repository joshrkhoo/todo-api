from flask import Flask, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)
from monogodb import get_todos

@app.route("/todos")
def todos():
    todos = get_todos()
    return str(todos)
