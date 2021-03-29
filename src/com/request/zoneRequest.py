#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

from com.driver.zdns_driver import dns_zone_driver


""" 权威区 """
class ZoneRequest(object):

    def __init__(self):
        # self.manager = dns_zone_driver.get_instance()
        self.manager = dns_zone_driver()
        

    def index(self):
        return {"Information": "The url is for DNS Acl RestApi "
                "interface"}

    '''
    get the list of zones of zdns_driver
    http://ip:port/v3/dns/zones/list?view_id=:id
    '''
    def list(self, view_id):
        if str(view_id) == 0 :
            return {
                'error':'400',
                'message':'view_id or zone_id is inqure'
                }
        # LOG.info(_("get the all of zones of dns from zdns_driver,view_id is %(view_id)s"), {"view_id": view_id})
        # get the all of zones
        context=None
        zones = self.manager.get_zones_driver(view_id)
        # LOG.info(_("get the all of zones of dns from zdns_driver done,response is %(zones)s"), {"zones": zones})
        return zones
    
    '''
    get the one of zones of zdns_driver
    http://ip:port/v3/dns/zones/show?view_id=123&zone_id=123
    '''
    def show(self, **args):
        
        if args.get('view_id',-1) or args.get('zone_id',-1):
            view_id=args.get('view_id')
            zone_id=args.get('zone_id')
        else:
            return {
                'error':'400',
                'message':'view_id or zone_id is inqure'
                }

        # LOG.info(_("get the one of zones of dns from zdns_driver,args is %(args)s"), {"args": str(args)})

        # get the one of zones 
        # fix error 
        zones = self.manager.get_zone_one_driver(view_id,zone_id)
        # LOG.info(_("get the one of zones of dns from zdns_driver done,response is  %(zones)s"), {"zones": str(zones)})
        return zones
