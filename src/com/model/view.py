#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

from com.config.config import Config
import uuid


class ViewModel(object):
    
    def __init__(self,name,priority,acls,href,owners,dns64s,fail_forwarder,zones,comment,aclList):
        self.config = Config.get_instance()
        self.name= name
        self.priority = priority
        self.acls = acls
        self.href = href
        self.owners = owners
        self.dns64s = dns64s
        self.fail_forwarder = fail_forwarder
        self.zones = zones
        self.zones = ""
        self.comment = comment
        self.view_id = ''.join(str(uuid.uuid1()).split('-'))
        self.zdns_view_id = ''.join(str(uuid.uuid1()).split('-'))
        self.view_zdns_view_id = ''.join(str(uuid.uuid1()).split('-'))
        self.view_acl_id = ''.join(str(uuid.uuid1()).split('-'))
        
        self.toJsonString()
        self.toSqlString(aclList)
    
    """ 组合后输出为json对象，方便请求dns创建服务 """
    def toJsonString(self):
        pass
    
    """ 组合sql模板输出SQL语句 """
    def toSqlString(self,aclList):
        # 查询acls中的acl_id
        acl_id={}
        acl_id[0]=""
        acl_index=0
        for aclName in self.acls:
            for acl in aclList:
                if acl.name == aclName:
                    print(acl.acl_id,':',acl.name)
                    acl_id[acl_index]=acl.acl_id
                    acl_index +=1

        self.sql = self.config.view_table_insert % (
                        self.view_id,
                        self.config.pool_id,
                        self.config.tenant_id,
                        self.name
                    ) + "\n" + self.config.zdns_view_info_t_table_insert % (
                        self.zdns_view_id,
                        self.name,
                        self.dns64s,
                        self.owners,
                        self.fail_forwarder,
                        self.config.current_users,
                        self.priority,
                        self.href,
                        self.zones,
                        self.comment
                    ) + "\n" + self.config.view_zdns_view_associations_table_insert %(
                        self.view_zdns_view_id,
                        self.view_id,
                        self.zdns_view_id
                    ) + "\n" + self.config.view_acl_associations_table_insert %(
                        self.view_acl_id,
                        acl_id[0],
                        self.view_id
                    )

        return self.sql

