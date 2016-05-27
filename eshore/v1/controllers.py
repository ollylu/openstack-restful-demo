from eshore.common.controllers import Controller
from eshore.common import exceptions
from eshore.db import api
from eshore.auth import api as auth_api


class UserController(Controller):

    @staticmethod
    def create(context):
        if auth_api.check_auth():
            status = api.create_user(context)
            if status:
                return {
                    "status": "OK"
                }
            else:
                return {
                    "status": 'False'
                }
        else:
            raise exceptions.Unauthorized

    @staticmethod
    def show(context, user_id):
        user = api.show_users(user_id)
        return {
            "user_name": user.name
        }


