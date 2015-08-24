# coding:utf-8

from flask import Flask
from flask_restful import Api
from ems.conf.Default import Config
from ems.actions.UserQueryAction import UserQueryAction
from ems.actions.UserCreateAction import UserCreateAction

app = Flask(
    Config.APP_NAME,
    static_folder=Config.STATIC_FOLDER,
    static_path=Config.STATIC_PATH)
api = Api(app)

# 定义url映射
api.add_resource(UserQueryAction, '/user/query')
api.add_resource(UserCreateAction, '/user/create')

if __name__ == '__main__':
    app.run(host=Config.EMS_HOST,
            port=Config.EMS_PORT,
            debug=Config.DEBUG)
