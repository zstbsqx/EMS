from flask import request
from flask_restful import Resource
from ..models import models

class Test(Resource):
    def get(self):
        return models.User.get()
        #return 'test!' + request.args.get('p', 'no param')
