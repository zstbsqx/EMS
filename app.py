from flask import Flask, request
import conf
# from flask_restful import resource

app = Flask(conf.APP_NAME,
            static_folder=conf.STATIC_FOLDER,
            static_path=conf.STATIC_PATH)

if __name__ == '__main__':
    app.run(host=conf.EMS_HOST,
            port=conf.EMS_PORT)
