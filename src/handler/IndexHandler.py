#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello ' + ', This is test !')
