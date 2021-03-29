#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import uuid
import sys
from com.util.sqlOutFile import SqlOutFile
from com.service import sqlSevice
from com.config.config import Config


class DnsSyncController(object):
    
    def __init__(self):
        self.config = Config.get_instance()
        self.out = SqlOutFile()
    
    def createSql(self):
        # 创建sql服务
        self.sqlSevice = sqlSevice.SqlSevice()
        # 运行acl
        self.sqlSevice.startAcl()
        # 运行view
        self.sqlSevice.startView()
        # 运行view
        self.sqlSevice.startZone()
        # 获取生产的所有sql
        allSqlList = self.sqlSevice.getAllSql()
        # 输出sql到文件中
        print("All Sql is Done")
        self.out.writeSqlFileToPath(allSqlList,self.config.sqlFileName)


# if __name__=="__main__":
#     for arg in sys.argv[1:]:
#         print(arg)
    
#     dnsSync = DnsSyncController()
#     dnsSync.createSql()
