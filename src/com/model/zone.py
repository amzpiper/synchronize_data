#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

from com.config.config import Config
import uuid


class ZoneModel(object):
    
    def __init__(self,name,rrs,default_ttl,ad_controller,renewal,owners,comment,masters,slaves):
        self.config = Config.get_instance()
        self.name= name
        self.rrs = rrs
        self.default_ttl = default_ttl
        self.ad_controller = ad_controller
        self.renewal = renewal
        self.owners = owners
        self.comment = comment
        self.masters = masters
        self.slaves = slaves
        
        self.version="version"
        self.refresh="refresh"
        self.retry="retry"
        self.expire="expire"
        self.minimum="minimum"
        self.serial="serial"
        self.deleted="false"
        self.status="status"
        self.action="action"
        self.reverse_name = self.name[::-1]
        self.shard="shard"

        self.value="value"

        # TODO 整理表关系，整理生成SQL关系
        self.zone_id = uuid.uuid1()
        self.zone_attributes_id = uuid.uuid1()
        self.zdns_zones_info_id = uuid.uuid1()
        self.zones_zdns_zone_id = uuid.uuid1()
        self.tenant_id = uuid.uuid1()
        
        self.toJsonString()
        self.toSqlString()
    
    """ 组合后输出为json对象，方便请求dns创建服务 """
    def toJsonString(self):
        pass
    
    """ 组合sql模板输出SQL语句 """
    def toSqlString(self,):
        self.sql = self.config.zone_table_insert % (
                        self.zone_id,self.version,self.name,
                        self.default_ttl,self.refresh,self.retry,
                        self.expire,self.minimum,self.serial,
                        self.deleted,self.status,self.action,
                        self.config.pool_id,self.reverse_name,self.shard
                    ) + "\n" + self.config.zone_attributes_table_insert % (
                        self.zone_attributes_id,
                        self.version,
                        self.value,
                        self.zone_id
                    ) + "\n" + self.config.zdns_zones_info_t_table_insert % (
                        self.zdns_zones_info_id,
                        self.name,
                        self.default_ttl
                    ) + "\n" + self.config.zones_zdns_zone_associations_table_insert % (
                        self.zones_zdns_zone_id,
                        self.zone_id,
                        self.zdns_zones_info_id
                    )

        return self.sql

