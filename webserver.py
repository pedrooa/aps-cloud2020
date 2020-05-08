from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal
import os
import subprocess

task_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

app = Flask(__name__)
api = Api(app)


class TaskListAPI(Resource):
    def __init__(self):

        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('pyproject', type=str, required=True,
        #                            help='No python project provided', location='json')
        self.reqparse.add_argument('pyproject')
        # self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    def get(self):
        # tarefas = list(taskCollection.find())
        # return {'tarefas': [marshal(tarefa, task_fields) for tarefa in tarefas]}
        return {"Oi"}

    def post(self):
        args = self.reqparse.parse_args()
        args = args['pyproject']
        pyproject = open("../docker/pyproject.py", "w")
        pyproject.write(args)
        pyproject.close()
        subprocess.call(['./dockerscript'])
        file = "../docker/result.txt"
        with open(file, 'r') as result:
            result = result.read()
        # print(args['pyproject'])
        # task = args['pyproject']
        # task = {
        #     'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
        #     'title': args['title'],
        #     'description': args['description'],
        #     'done': False
        # }
        # taskCollection.insert_one(task)
        # return {'task': marshal(task, task_fields)}, 201
        return {'task': result}, 201


class HealthcheckAPI(Resource):

    def get(self):
        return {}, 200


api.add_resource(TaskListAPI, '/tarefas', endpoint='tarefas')
api.add_resource(HealthcheckAPI, '/healthcheck', endpoint='healthcheck')

if __name__ == '__main__':

    app.run(host=os.getenv('LISTEN', '0.0.0.0'), port=int(
        os.getenv('PORT', '8080')), debug=True)
