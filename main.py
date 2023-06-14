from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
from monogodb import get_todos


@app.route("/todos")
def todos():
    todos = get_todos()
    todo_list = []
    for todo in todos:
        todo_dict = {
            'id': str(todo['_id']),
            'title': todo['title'],
            'description': todo['description']
        }
        todo_list.append(todo_dict)
    return jsonify(todo_list)
