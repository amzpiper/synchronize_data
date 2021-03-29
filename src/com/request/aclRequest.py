#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

from requests.models import Response
from com.driver.zdns_driver import dns_zone_driver
#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

# 查询acl
class AclRequest(object):

    def __init__(self):
        # self.manager = dns_zone_driver.get_instance()
        self.manager = dns_zone_driver()
    
    """  """
    def index(self):
        print("aclDao")
        return {"Information": "The url is for DNS Acl RestApi "
                "interface"}

    '''
    get the list of acls from zdns_driver
    http://ip:port/v3/dns/acls/list
    '''
    def list(self):
        response = self.manager.get_acls_driver()
        return response

    '''
    get the one of acls from zdns_driver
    http://ip:port/v3/dns/acls/show?acl_id=:acl_id
    '''
    def show(self, acl_id):
        if str(acl_id) == 0 :
            return {
                'error':'400',
                'message':'view_id or zone_id is inqure'
                }
        acl = self.manager.get_acl_one_driver(acl_id)
        return acl