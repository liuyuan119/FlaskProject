from flask_restful import Resource


class UserResource(Resource):

    def get(self):
        return {"msg": "user get"}

    def post(self):

        return {"msg": "user post"}