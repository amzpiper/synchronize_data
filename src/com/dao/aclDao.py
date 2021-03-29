#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import json
from com.request import aclRequest
from com.config.config import Config
from com.model import acl

""" 处理把response返回的dict对象中内容处理后放到acl对象数组中 """
class AclDao(object):

    def __init__(self) :
        self.aclList = []
        self.aclReq = aclRequest.AclRequest()
        self.config = Config.get_instance()

    """ 请求并解析acl的json返回结果,把所有json中的acl整理成acl对象，再存入到1个list中 """
    def getAcl(self):
        print("Acl is Going to get response ...")
        response = self.aclReq.list()
        # 当响应返回错误时
        if response.get("error","true") != "true":
            print("Acle get list Error ...")
            raise Exception
        print("Acl got response.All is %s..." % response['total_size'])

        print("Acl is Creating Sql ...")
        for item in response['resources']:
            self.aclList.append(acl.AclModel(item['name'],item['networks'],item['href']))
            self.config.acl_count += 1
            print("Acl Sql is Create %s ..." % self.config.acl_count)
        print("Acl Sql is Done ...")

        return self.aclList
