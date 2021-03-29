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
        
        self.version="1"
        self.refresh="3500"
        self.retry="600"
        self.expire="86400"
        self.minimum="3600"
        self.serial=round(1999999999)
        self.deleted="0"
        self.status="ACTIVE"
        self.action="NONE"
        self.reverse_name = self.name[::-1]
        self.shard="6"

        self.key="pool_id"
        self.value=self.config.pool_id_not_split_

        # TODO 整理表关系，整理生成SQL关系
        self.zone_id = ''.join(str(uuid.uuid1()).split('-'))
        self.zone_attributes_id = ''.join(str(uuid.uuid1()).split('-'))
        self.zdns_zones_info_id = ''.join(str(uuid.uuid1()).split('-'))
        self.zones_zdns_zone_id = ''.join(str(uuid.uuid1()).split('-'))
        
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
                        self.key,
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

