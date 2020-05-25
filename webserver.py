from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal
import os
import subprocess

app = Flask(__name__)
api = Api(app)


class TaskListAPI(Resource):
    def __init__(self):

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('pyproject')
        super(TaskListAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        args = args['pyproject']
        pyproject = open("../docker/pyproject.py", "w")
        pyproject.write(args)
        pyproject.close()
        os.system("./dockerscript")
        file = "../docker/result.txt"
        with open(file, 'r') as result:
            result = result.read()
        return {'task': result}, 201


class HealthcheckAPI(Resource):

    def get(self):
        return {}, 200


api.add_resource(TaskListAPI, '/tarefas', endpoint='tarefas')
api.add_resource(HealthcheckAPI, '/healthcheck', endpoint='healthcheck')

if __name__ == '__main__':
    app.run(host=os.getenv('LISTEN', '0.0.0.0'), port=int(
        os.getenv('PORT', '8080')), debug=True)
