from eshore.common.controllers import Controller
from eshore.common import exceptions
from eshore.db import api
from eshore.auth import api as auth_api
import webob.exc


class UserController(Controller):

    @staticmethod
    def create(context):
        if auth_api.check_auth():
            status = api.create_user(context)
            return {
                "status": status
            }
        else:
            raise exceptions.Unauthorized

    @staticmethod
    def show(context, user_id):
        user = api.show_users(user_id)
        if user:
            return {
                "user_name": user.name
            }
        else:
            raise webob.exc.HTTPNotFound()


