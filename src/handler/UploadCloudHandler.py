#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.web
import qiniu.config
import string, os, sys
import json

# CUR_PATH = os.path.abspath(os.curdir)
CUR_PATH = os.path.abspath(__file__)
sys.path.append(os.path.abspath(os.path.join(CUR_PATH, "../../../")))
sys.path.append(os.path.abspath(os.path.join(CUR_PATH, "../../../tinder/python")))

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
from conf.config import LOGFILE, MTYPE, QN
from util.helpers.log_helper import get_logger

LOG = get_logger(log_file_path = LOGFILE, backupCount=50)

class UploadCloudHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Sorry, GET method is not supported by the cloudstore Service, Please use POST !")

    def post(self):

        status = 0
        try:
            upload_path = os.path.join(os.path.dirname(__file__), '../tmpfiles')

        except Exception as e:
            status = 1
            message = "dir is not exist, please check local dir!"
            data = ""
            respon_json = Respon(status, data, message)
            LOG.info("%s" % message)
            return

        try:
            file_metas=self.request.files['file']

        except Exception as e:
            status = 1
            message = "file can't open, please check the permissions of the file"
            data = ""
            response_json = response(status, data, message)
            LOG.info("%s" % message)
            return

        if status == "1":
            self.write(response_json)

        for meta in file_metas:
            filename = meta['filename']
            file_path = os.path.join(upload_path, filename)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])

        key = self.get_argument('key')
        media_type = self.get_argument('type')

        if checkparameter(media_type):
        # 七牛上传接口
            q = Auth(QN['AKEY'], QN['SKEY'])
            if media_type == "image":
                token = q.upload_token(QN['IMGBUCTET'], key)
                ret, info = put_file(token, key, file_path)

                if ret['key']:
                    message = "upload success"
                    response_json = response(status, QN['IMGURL'] + '/' + key, message)
                    LOG.info("%s/%s" % (QN['IMGURL'], key))
                    self.write(response_json)

                else:
                    status = 1
                    message = "upload fail, please check post data and file!"
                    data = ""
                    response_json = response(status, data, message)
                    LOG.info("%s" % message)
                    self.write(response_json)

            else:
                token = q.upload_token(QN['VDOBUCTET'], key)
                ret, info = put_file(token, key, file_path)

                if ret['key']:
                    message = "upload success"
                    response_json = response(status, QN['VDOURL'] + '/' + key, message)
                    LOG.info("%s/%s" % (QN['VDOURL'], key))
                    self.write(response_json)

                else:
                    status = 1
                    message = "upload fail, please check post data and file!"
                    data = ""
                    response_json = response(status, data, message)
                    LOG.info("%s" % message)
                    self.write(response_json)
               
        else:
            status = 1
            message = "post params error, please check !"
            data = ""
            response_json = response(status, data, message)
            LOG.info("%s" % message)
            self.write(response_json)

def checkparameter(mtype):

    if mtype in MTYPE:
        return True

    return False


def response(status, data, message):
    response = [{"status":status, "data":data, "message":message}]
    response_json = json.dumps(response)
    return response_json
