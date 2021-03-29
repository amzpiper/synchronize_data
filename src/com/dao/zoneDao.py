#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang
from com.request import zoneRequest
from com.config.config import Config
from com.model import zone
import abc

class ZoneDao(object):

    def __init__(self) :
        self.zoneList = []
        self.zoneReq = zoneRequest.ZoneRequest()
        self.config = Config.get_instance()

    """ 请求并解析viewReq的json返回结果,把所有json中的view整理成view对象，再存入到1个list中 """
    def getZone(self,viewList):
        print("Zone is Going to get response,View_count is %s..." % self.config.view_count)
        # 循环获取所有view下的zone
        count=0
        for view in viewList:
            response = self.zoneReq.list(view_id=view.name)
            # 当响应返回错误时
            if response.get("error","true") != "true":
                print("Zone get list Error ...")
                raise Exception

            count+=1
            print("Zone got response %s/%s" % (count,self.config.view_count))

            print("Zone is Creating Sql ...")
            for item in response['resources']:
                # print(item)
                self.zoneList.append(zone.ZoneModel(
                    item['name'],
                    item['rrs'],
                    item['default_ttl'],
                    item['ad_controller'],
                    item['renewal'],
                    item['owners'],
                    item['comment'],
                    item['masters'],
                    item['slaves']
                ))
                self.config.zone_count += 1
                print("Zone Sql is Create %s ..." % self.config.zone_count)
        print("Zone Sql is Done ...")
        
        return self.zoneList