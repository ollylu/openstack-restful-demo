import routes

from eshore import wsgi
from eshore.v1 import controllers


class API(wsgi.Router):
    def __init__(self, mapper=None):
        if mapper is None:
            mapper = routes.Mapper()

        controller = controllers.UserController()
        mapper.connect("/users",
                       controller=controller,
                       action="create",
                       conditions=dict(method=['POST']))
        mapper.connect("/users/{user_id}",
                       controller=controller,
                       action="show",
                       conditions=dict(method=['GET']))

        super(API, self).__init__(mapper)
