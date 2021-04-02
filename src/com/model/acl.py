#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

from com.config.config import Config
import uuid


class AclModel(object):
    
    def __init__(self,name,networks,href):
        self.config = Config.get_instance()
        self.name= name
        self.networks = networks
        self.href = href
        self.acl_id = ''.join(str(uuid.uuid1()).split('-'))
        self.zdns_acl_id = ''.join(str(uuid.uuid1()).split('-'))
        self.acl_zdns_acl_id = ''.join(str(uuid.uuid1()).split('-'))
        self.toJsonString()
        self.toSqlString()

    """ 组合后输出为dict对象 """
    def toJsonString(self):
        self.dict={
           "name": self.name,
           "networks": self.networks,
           "pool_id": self.config.pool_id
        }
        return self.dict
    
    """ 组合sql模板输出SQL语句 """
    def toSqlString(self):
        self.sql = self.config.acl_table_insert % (
                        self.acl_id,
                        self.config.pool_id,
                        self.config.tenant_id,
                        self.name,
                        self.networks
                    ) + "\n" + self.config.zdns_acl_info_t_table_insert % (
                        self.zdns_acl_id,
                        self.name,
                        self.networks,
                        self.config.current_users,
                        self.href,
                        "comment"                  
                    ) + "\n" + self.config.acl_zdns_acl_associations_table_insert %(
                        self.acl_zdns_acl_id,
                        self.acl_id,
                        self.zdns_acl_id
                    )
        return self.sql 
