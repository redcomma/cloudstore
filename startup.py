#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

from tornado.options import define, options
from conf.config import PORT
from url import url

define("port", default=PORT, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = url
        tornado.web.Application.__init__(self, handlers)

def response(status, data, message):
    response = [{"status":status, "data":data, "message":message}]
    response_json = json.dumps(response)
    return response_json

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
