#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Copyright (c) 2017. All Rights Reserved
    @author: (liyang@liyang.com)
    @brief: qiniu test
"""
import os.path
config_path = os.path.dirname(os.path.abspath(__file__)) # 当前的文件路径


# 服务启动端口
PORT = 8000

# 日志路径
LOGPATH = "%s/../logs/" % config_path

# 日志文件
LOGFILE = "%s/tornado.log" % LOGPATH

# 媒介类型
MTYPE = ["test1","test2"]

# 七牛访问参数
QN = {  'IMGURL': 'http://www.redcomma.com', 
        'VDOURL': 'http://www.liyang.com', 
        'AKEY': 'xxxxxxxxxxxxxxxxx',
        'SKEY': 'yyyyyyyyyyyyyyyyy',
        'IMGBUCTET': 'testbuck1',
        'VDOBUCTET': 'testbuck2',
 }
