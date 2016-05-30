import routes

from eshore import wsgi
from eshore.v1 import controllers


class API(wsgi.Router):
    def __init__(self, mapper=None):
        if mapper is None:
            mapper = routes.Mapper()

        controller = controllers.UserController()
        """
        @api {post} /users Create New User
        @apiName CreateUser
        @apiGroup User

        @apiParam {Number} id Users unique ID.
        @apiParam {String} name User's name.
        @apiParam {String} password User's password.

        @apiSuccess {String} status Result.
        """
        mapper.connect("/users",
                       controller=controller,
                       action="create",
                       conditions=dict(method=['POST']))
        """
        @api {get} /user/:user_id Request User information
        @apiName GetUser
        @apiGroup User

        @apiParam {Number} user_id Users unique ID.

        @apiSuccess {String} user_name name of the User.
        """
        mapper.connect("/users/{user_id}",
                       controller=controller,
                       action="show",
                       conditions=dict(method=['GET']))

        super(API, self).__init__(mapper)
