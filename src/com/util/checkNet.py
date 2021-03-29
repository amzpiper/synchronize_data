#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import uuid
import sys

from requests.api import request
from com.controller.DnsSyncController import DnsSyncController
from com.config.config import Config
from com.driver.zdns_driver import dns_zone_driver


class CheckNet(object):
    
    def __init__(self):
        # self.config = Config.get_instance()        
        self.request = dns_zone_driver.get_instance()
        response = self.request.check_network()
    
        # 如果网络请求失败,结束
        if response.get("error") != None:
            print("response: %s" % response)
            print("please check network or url is work!")
            pass
        else:
            print("url is check OK!")

if __name__=="__main__":
    CheckNet()