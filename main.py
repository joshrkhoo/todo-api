#Importing libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from todo import Todo
import datetime



# creating Flask app by name of file ?
app = Flask(__name__)
CORS(app)
from monogodb import get_todos, post_todo

#route the app as /todos (this will be put after the web url: 'http://127.0.0.1:5000/todos')
@app.route("/todos", methods=['GET'])
def get_all_todos():
    todos = get_todos()
    print(todos)
    todo_dicts = []
    for todo in todos:
        dict_todo = todo._asdict()
        todo_dicts.append(dict_todo)
    return jsonify(todo_dicts)


@app.route('/todos', methods=['POST'])
def new_todo():

    todo_data = request.get_json()
    
    # new_tod'_id'
    #     'title': todo_data.get('title'),
    #     'description': todo_data.get('description'),
    #     'date_created': todo_data.get('date_created'),
    #     'status': False
    # }

    new_todo = Todo(
        title = todo_data.get('title'),
        description = todo_data.get('description'),
        datetime_created = datetime.datetime.now(),
        status = False,
        id = None
    )   

    res = post_todo(new_todo)

    if res.inserted_id:
        # Return a JSON response indicating success
        response = {'success': True, 'message': 'Data added successfully'}
        return jsonify(response), 200
    else:
        # Return a JSON response indicating failure
        response = {'success': False, 'message': 'Data insertion failed'}
        return jsonify(response), 400




@app.route("/todos/<todo_id>", methods = ['DELETE'])
def delete_todo():
    

    



