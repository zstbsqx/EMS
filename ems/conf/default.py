#!usr/bin/python
# coding:utf-8


class Config(object):
    # host settings
    EMS_HOST = '0.0.0.0'
    EMS_PORT = 9001
    DEBUG = True

    STATIC_FOLDER = 'static'
    STATIC_PATH = '/res'

    # Database settings
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 3306
    DATABASE_USER = 'EMS'
    DATABASE_PASSWORD = '123456'
    DATABASE_NAME = 'EMS'

    # app settings
    APP_NAME = 'EMS'

    CHECK_USER_LOGIN = 0
    CHECK_USER_AUTHORITY = 0
