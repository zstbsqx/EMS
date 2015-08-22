from flask import Flask, resource, request
from flask.ext.restful import resource

app = Flask('EMS', static_folder = 'static', static_path = '/res')

if __name__ == '__main__':
  app.run()