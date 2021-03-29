#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import sys  
import com.dao.aclDao as aclDao
import com.dao.viewDao as viewDao
import com.dao.zoneDao as zoneDao
from com.config.config import Config

""" 把response返回的view对象数组处理一下 """
class SqlSevice(object):

    def __init__(self):
        self.config = Config.get_instance()
        self.aclDao = aclDao.AclDao()
        self.viewDao = viewDao.ViewDao()
        self.zoneDao = zoneDao.ZoneDao()
        # 储存所有查出来的对象
        self.aclList=None
        self.viewList=None
        self.zoneList=None
        # 储存所有查出来的对象生产的sql
        self.sqlList = []
        self.aclSqlList = []
        self.viewSqlList = []
        self.zoneSqlList = []
        print("SqlSevice is Beging!")

    """ 获取所有acl对象的数据 """
    def startAcl(self):
        # 查询所有acl数据并生产sql
        self.aclList = self.aclDao.getAcl()
        for acl in self.aclList:
            # print(item.sql)
            self.aclSqlList.append(acl.sql)
            self.sqlList.append(acl.sql)
        #个数 
        print("Acl_count:%s" % self.config.acl_count)
        print("Acl is All Done")
        return self.aclList

    """ 获取所有view对象的数据 """
    def startView(self):
        # 查询所有view数据并生产sql
        self.viewList = self.viewDao.getView(self.aclList)
        for view in self.viewList:
            # print(item.sql)
            self.viewSqlList.append(view.sql)
            self.sqlList.append(view.sql)
        #个数 
        print("View_count:%s" % self.config.view_count)
        print("View is All Done")
        return self.viewList

    """ 获取所有zone对象的数据 """
    def startZone(self):
        # 查询所有view下所有zone数据并生产sql
        self.zoneList = self.zoneDao.getZone(self.viewList)
        for zone in self.zoneList:
            # print(item.sql)
            self.zoneSqlList.append(zone.sql)
            self.sqlList.append(zone.sql)
        #个数 
        print("Zone_count:%s" % self.config.zone_count)
        return self.zoneList

    """ 获取acl所有sql """
    def getAclSql(self):
        for sql in self.aclSqlList:
            print(sql)
        return self.aclSqlList

    """ 获取view所有sql """
    def getViewSql(self):
        for sql in self.viewSqlList:
            print(sql)
        return self.viewSqlList

    """ 获取zone所有sql """
    def getZoneSql(self):
        for sql in self.zoneSqlList:
            print(sql)
        return self.zoneSqlList

    """ 获取所有sql """
    def getAllSql(self):
        # for sql in self.sqlList:
            # print(sql)
        return self.sqlList

    