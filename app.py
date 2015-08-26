# coding:utf-8

from flask import Flask
from flask_restful import Api
from ems.conf.Default import Config
from ems.actions.UserQueryAction import UserQueryAction
from ems.actions.LoginAction import LoginAction
from ems.actions.LogoutAction import LogoutAction
from ems.actions.UserCreateAction import UserCreateAction
from ems.actions.UserListAction import UserListAction
from ems.actions.EventListAction import EventListAction

app = Flask(
    Config.APP_NAME,
    static_folder=Config.STATIC_FOLDER,
    static_path=Config.STATIC_PATH)
app.secret_key = 'lfwsb'
api = Api(app)


# 定义url映射
api.add_resource(LoginAction, '/user/login')
api.add_resource(LogoutAction, '/user/logout')
api.add_resource(UserCreateAction, '/user/create')
api.add_resource(UserQueryAction, '/user/query')
api.add_resource(UserListAction, '/user/list')
api.add_resource(EventListAction, '/event/list')

if __name__ == '__main__':
    app.run(host=Config.EMS_HOST,
            port=Config.EMS_PORT,
            debug=Config.DEBUG)
