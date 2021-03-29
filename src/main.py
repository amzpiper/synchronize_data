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


class Main(object):
    
    def __init__(self):
        self.request = dns_zone_driver.get_instance()
        response = self.request.check_network()
        
        # 如果网络请求失败,结束
        if response.get("error") != None:
            print("response: %s" % response)
            print("please check network or url is work!")
            pass
        else:
            # print("网络测试正常,开始执行脚本...")
            print("script is begging!")
            dnsSync = DnsSyncController()
            dnsSync.createSql()


if __name__=="__main__":
    # for arg in sys.argv[1:]:
    #     print(arg)
    Main()