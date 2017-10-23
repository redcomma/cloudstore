#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from src.handler.IndexHandler import IndexHandler
from src.handler.UploadCloudHandler import UploadCloudHandler

url = [
        (r'/', IndexHandler),
        (r'/upload', UploadCloudHandler)
    ]
