import logging
import routes.middleware
import webob.dec
import webob.exc


class Router(object):

    def __init__(self, mapper=None):
        print "Router.__init__"
        self.map = mapper
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.map)

    @classmethod
    def factory(cls, global_conf, **local_conf):
        print "Router.__factory__"
        return cls()

    @webob.dec.wsgify
    def __call__(self, req):
        print "Router.__call__"
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        print "Router._dispatch"
        # TODO
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()
        app = match['controller']
        return app
