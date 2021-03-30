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


class Test(object):
    
    def __init__(self):
        self.config = Config.get_instance()
        self.request = dns_zone_driver.get_instance()


    def test(self):
        self.config.profile = "test"
        self.config.sqlFilePath = "E:"
        dnsSync = DnsSyncController()
        dnsSync.createSql()

if __name__=="__main__":
    main = Test()
    main.test()
