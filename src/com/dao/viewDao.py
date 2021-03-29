#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import json
from com.request import viewRequest
from com.config.config import Config
from com.model import view

""" 处理把response返回的dict对象中内容处理后放到view对象数组中 """
class ViewDao(object):

    def __init__(self) :
        self.viewList = []
        self.viewReq = viewRequest.ViewRequest()
        self.config = Config.get_instance()

    """ 请求并解析viewReq的json返回结果,把所有json中的view整理成view对象，再存入到1个list中 """
    def getView(self,aclList):
        print("View is Going to get response ...")
        response = self.viewReq.list()
        # 当响应返回错误时
        if response.get("error","true") != "true":
            print("View get list Error ...")
            raise Exception

        print("View got response.All is %s..." % response['total_size'])

        print("View is Creating Sql ...")
        for item in response['resources']:
            # print(item)
            self.viewList.append(view.ViewModel(
                item['name'],
                item['priority'],
                item['acls'],
                item['href'],
                item['owners'],
                item['dns64s'],
                item['fail_forwarder'],
                item['zones'],
                item['comment'],
                aclList
            ))
            self.config.view_count += 1
            print("View Sql is Create %s ..." % self.config.view_count)
        print("View Sql is Done ...")
        
        return self.viewList
