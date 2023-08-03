#Importing libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from todo import Todo
import datetime
import pytz



# creating Flask app by name of file ?
app = Flask(__name__)
CORS(app)
from monogodb import get_todos, post_todo, delete_todo

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
def post_new_todo():

    todo_data = request.get_json()
    timezone = pytz.timezone('Australia/Sydney')
    
    # new_tod'_id'
    #     'title': todo_data.get('title'),
    #     'description': todo_data.get('description'),
    #     'date_created': todo_data.get('date_created'),
    #     'status': False
    # }

    new_todo = Todo(
        title = todo_data.get('title'),
        description = todo_data.get('description'),
        datetime_created = datetime.datetime.now(timezone),
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




@app.route("/todos/<todoid>", methods = ['DELETE'])
def delete_a_todo(todoid):
    print(todoid)
    res = delete_todo(todoid)

    # Check if the deletion was successful
    if res.deleted_count > 0:
        # Return a JSON response indicating success
        response = {'success': True, 'message': 'Todo deleted successfully'}
        return jsonify(response), 200
    else:
        # Return a JSON response indicating failure
        response = {'success': False, 'message': 'Todo not found'}
        return jsonify(response), 404


# @app.route("todos/<todoid>", methods = ['PUT'])
# def update_a_todo(editId):

#     res = update_todo(editId)

#     if res.matched_count > 0:
#         return jsonify({'message': f'Todo with ID {editId} has been updated.'}), 200
#     else:
#         return jsonify({'error': 'Todo not found.'}), 404




#run the app
if __name__ == "__main__":
    app.run(debug=True)

