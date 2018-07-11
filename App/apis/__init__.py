from flask_restful import Api

from App.apis.HelloApi import HelloResource
from App.apis.UserApi import UserResource

api = Api()


def init_api(app):
    api.init_app(app=app)


api.add_resource(HelloResource, "/hello/")

api.add_resource(UserResource, "/user/")
