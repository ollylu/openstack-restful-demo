import webob.dec
from webob import Response
import webob.exc
import json
from eshore.common import exceptions


class Controller(object):
    @webob.dec.wsgify
    def __call__(self, req):
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        action = arg_dict.pop('action')
        del arg_dict['controller']
        params = arg_dict
        context = dict(req.params)
        if hasattr(self, action):
            try:
                method = getattr(self, action)
                result = method(context, **params)
                response = Response(request=req,
                                    content_type='application/json')
                response.body = json.dumps(result)
                return response
            except exceptions.Unauthorized:
                return webob.exc.HTTPUnauthorized()
        return webob.exc.HTTPNotFound()

