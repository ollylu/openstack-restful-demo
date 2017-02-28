# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `server`
    @Author : `long`
    @Date   : `2016-05-19`
    @About  : ''
"""

import os
import logging
import sys
from paste import deploy
from eventlet import wsgi
import eventlet
import config
from eshore.db import init_db


LOG = logging.getLogger(__name__)

module_dir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                           os.pardir, os.pardir))

sys.path.insert(0, module_dir)

bind_host = "127.0.0.1"
bind_port = 8088


def server(app_name, conf_file):
    print "server"
    app = load_paste_app(app_name, conf_file)
    # eventlet.monkey_patch()
    # wsgi.server(eventlet.listen((bind_host, bind_port)), app)
    from gevent.wsgi import WSGIServer
    from gevent import monkey
    monkey.patch_all()
    http_server = WSGIServer(('', bind_port), app)
    http_server.serve_forever()


def load_paste_app(app_name, conf_file):
    print "load_paste_app"
    LOG.debug("Loading %(app_name) from %(conf_file)",
              {'app_name': app_name, 'conf_file': conf_file})

    try:
        app = deploy.loadapp("config:%s" % conf_file, name=app_name)
        return app
    except (LookupError, ImportError) as e:
        LOG.error(str(e))
        raise RuntimeError(str(e))


if __name__ == '__main__':
    init_db()
    server(config.APP_NAME, config.PASTE_CONFIG)
