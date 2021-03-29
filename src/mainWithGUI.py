#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import uuid
import sys

from requests.api import request
from com.util.sqlOutFile import SqlOutFile
from com.controller.DnsSyncController import DnsSyncController
from com.config.config import Config
from com.driver.zdns_driver import dns_zone_driver


class MainWithGUI(object):

    def __init__(self):
        self.config = Config.get_instance()

    # 修改配置 
    def editConfig(self,):
        pass

    # 检测网络
    def checkNet(self):
        self.request = dns_zone_driver.get_instance()
        response = self.request.check_network()
    
        # 如果网络请求失败,结束
        if response.get("error") != None:
            print("response: %s" % response)
            print("please check network or url is work!")
            pass
        else:
            print("url is check OK!")
    
    # 创建sql
    def createSql(self):
        dnsSync = DnsSyncController()
        dnsSync.createSql()

if __name__=="__main__":
    # for arg in sys.argv[1:]:
    #     print(arg)
    MainWithGUI()
