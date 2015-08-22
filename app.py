from flask import Flask, request
from flask_restful import Api

from EMS.actions.test import Test

app = Flask('EMS', static_folder = 'static', static_path = '/res')
api = Api(app)

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(debug = True)