# coding:utf-8

from flask import Flask
from flask_restful import Api
from ems.conf.config import Config

app = Flask(
    Config.APP_NAME,
    static_folder=Config.STATIC_FOLDER,
    static_path=Config.STATIC_PATH)
api = Api(app)

# 定义url映射
from ems.actions.test import Test
api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(host=Config.EMS_HOST,
            port=Config.EMS_PORT,
            debug=Config.DEBUG)
