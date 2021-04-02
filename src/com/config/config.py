#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang


DNS_DRIVER = None

# 配置中心
class Config(object):
    
    def __init__(self):
        # 开发模式 prop:生产;test:测试
        # self.profile = "test"
        self.profile = "prop"

        # zdns 配置
        self.host_ip = "55.15.66.46"
        self.port = 20120
        self.view_id = "default"
        self.auth_name = "admin"
        self.auth_pw = "zdns"

        
        self.check_network_url = "https://"+self.host_ip+":"+str(self.port)+"/acls"

        # 文件输出路径
        # self.sqlFilePath = "E:"
        self.sqlFilePath = "/home"
        self.sqlFileName = "allSql"

        # pool_id，根据实际情况修改
        self.pool_id="26fa967195d1466687c080daf31b2eca"
        self.pool_id_not_split_="36fa9671-95d1-4666-87c0-90daf31b2eca"
        self.current_users="admin"
        self.tenant_id="noauth-project"

        # 统计数量
        self.acl_count=0
        self.view_count=0
        self.zone_count=0

        # sql插入语句模板
        # acl三层表:done
        self.acl_table_insert='''
        insert into acl(id,pool_id,tenant_id,name,networks) 
        values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");'''
        # acl四层表
        self.zdns_acl_info_t_table_insert='''
        insert into zdns_acl_info_t(id,name,networks,current_users,href,`comment`) 
        values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");'''
        # acl三层和四层关联关系表
        self.acl_zdns_acl_associations_table_insert='''
        insert into acl_zdns_acl_associations(id,acl_id,zdns_acl_id) 
        values (\"%s\",\"%s\",\"%s\");'''

        # view三层表
        self.view_table_insert='''
        insert into view(id,pool_id,tenant_id,name) 
        values (\"%s\",\"%s\",\"%s\",\"%s\");'''
        # view四层表
        self.zdns_view_info_t_table_insert='''
        insert into zdns_view_info_t(id,name,dns64s,owners,fail_forwarder,current_users,priority,href,zones,`comment`) 
        values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%s,\"%s\",\"%s\",\"%s\");'''
        # view三层和四层关联关系表
        self.view_zdns_view_associations_table_insert='''
        insert into view_zdns_view_associations(id,view_id,zdns_view_id) 
        values (\"%s\",\"%s\",\"%s\");'''
        # view和acl关联关系表
        self.view_acl_associations_table_insert='''
        insert into view_acl_associations(id,acl_id,view_id) 
        values (\"%s\",\"%s\",\"%s\");'''

        # zone三次表
        self.zone_table_insert='''
        insert into zones(id,version,name,ttl,refresh,retry,expire,minimum,serial,deleted,status,action,pool_id,reverse_name,shard) 
        values (\"%s\",%s,\"%s\",%s,%s,%s,%s,%s,%s,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");'''
        # zone三层表
        self.zone_attributes_table_insert='''
        insert into zone_attributes(id,`version`,`key`,`value`,zone_id) 
        values (\"%s\",%s,\"%s\",\"%s\",\"%s\");'''
        # zone四层表
        self.zdns_zones_info_t_table_insert='''
        insert into zdns_zones_info_t(id,name,default_ttl) 
        values (\"%s\",\"%s\",%s);'''
        # zone关系表
        self.zones_zdns_zone_associations_table_insert='''
        insert into zones_zdns_zone_associations(id,zone_id,zdns_zone_id) 
        values (\"%s\",\"%s\",\"%s\");'''

    # 单例模式,获取当前对象
    @classmethod    
    def get_instance(cls):
        global DNS_DRIVER
        if not DNS_DRIVER:
            DNS_DRIVER = cls()
        return DNS_DRIVER

