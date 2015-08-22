from flask import Flask, request
from flask_restful import Api
from ems.actions.test import Test
from ems import conf

app = Flask(conf.APP_NAME,
            static_folder=conf.STATIC_FOLDER,
            static_path=conf.STATIC_PATH)
api = Api(app)

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(host=conf.EMS_HOST,
            port=conf.EMS_PORT,
            debug=True)

