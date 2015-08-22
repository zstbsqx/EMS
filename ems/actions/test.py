from flask import request
from flask_restful import Resource

class Test(Resource):
    def get(self):
        return 'test!' + request.args.get('p', 'no param')