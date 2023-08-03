from typing import List
from bson import ObjectId
from flask_pymongo import PyMongo
from main import app
from todo import Todo


app.config["MONGO_URI"] ="mongodb+srv://giganotosaurus:Joshpass01@todo-api.kwzhjvd.mongodb.net/development?retryWrites=true&w=majority"

mongo = PyMongo(app)
mongo.init_app(app)

# print(mongo)
# print(vars(mongo))


# Get the todos that are already in the mongodb
def get_todos() -> List[Todo]:

    elements = mongo.db.todos.find()
    todo_list = []

    for todo in list(elements):
        new_todo = Todo(
        title = todo.get('title'),
        description = todo.get('description'),
        datetime_created = todo.get('datetime_created'),
        status = False,
        id = str(todo.get('_id')))


        print(new_todo)
        todo_list.append(new_todo)
    # print(elements)


    return todo_list


def post_todo(new_todo):
    result = mongo.db.todos.insert_one(new_todo._asdict())
    return result


def delete_todo(todoid):
    print('hello world')
    obj_id = ObjectId(todoid)
    print(obj_id)
    print(todoid)
    result = mongo.db.todos.delete_one({'_id': obj_id})
    return result


# def update_todo(editId):
#     obj_id = ObjectId(editId)
#     todo = mongo.db.todos.find_one({'_id': obj_id})
#     result = mongo.db.todos.update_one(
#         {'_id': obj_id},
#     )

#     return result