from flask import Flask, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["MONGO_URI"] ="mongodb+srv://giganotosaurus:Joshpass01@todo-api.kwzhjvd.mongodb.net/development?retryWrites=true&w=majority"

mongo = PyMongo(app)
mongo.init_app(app)

print(mongo)
print(vars(mongo))

def get_todos():
    elements = mongo.db.todos.find()
    print(elements)
    return list(elements)


@app.route("/todos")
def todos():
    todos = get_todos()
    return str(todos)
