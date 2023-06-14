#Importing libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo



# creating Flask app by name of file ?
app = Flask(__name__)
CORS(app)
from monogodb import get_todos
mongo = PyMongo(app)

#route the app as /todos (this will be put after the web url: 'http://127.0.0.1:5000/todos')
@app.route("/todos", methods=['GET'])
def get_all_todos():
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


@app.route('/todos', methods=['POST'])
def new_todo():

    todo_data = request.get_json()
    
    new_todo = {
        'title': todo_data.get('title'),
        'description': todo_data.get('description'),
        'date_created': todo_data.get('date_created'),
        'status': False
    }

    result = mongo.db.todos.insert_one(new_todo)

    if result.inserted_id:
        # Return a JSON response indicating success
        response = {'success': True, 'message': 'Data added successfully'}
        return jsonify(response), 200
    else:
        # Return a JSON response indicating failure
        response = {'success': False, 'message': 'Data insertion failed'}
        return jsonify(response), 400




# @app.route("/todos/todo_id", methods = ['DELETE'])
# def delete_todo():




