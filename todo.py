from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

todos={
    1:{"task": "Write Hello world program", "summary":"wite the code using python."},
    2:{"task": "task2", "summary" : "Todo task 2."},
}

class ToDo(Resource):
    def get(self,todo_id):
        if todo_id not in todos:
            return {'message': 'Todo not found'}
        return todos[todo_id]
    
    def post(self,todo_id):
        data=request.get_json()
        if todo_id in todos:
            abort(409,message="Task already exist")

        else:
            todos[todo_id]=data
            return todos[todo_id]
    def put(self,todo_id):
        data = request.get_json()
        if todo_id not in todos:
            abort(404, message="Task not found")
        todos[todo_id]= data
        return todos[todo_id]
    

    def delete(self, todo_id):
        if todo_id not in todos:
            return {'message':'Invalid todo id'}
        else:
            del todos[todo_id]
            return {'mesage': 'Deleted todo'}
        
class ToDoList(Resource):
    def get(self):
        return todos

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')
if __name__ == '__main__':
    app.run(debug=True)