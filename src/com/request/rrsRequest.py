'''
Date:2021/3/19
Author:Guoyha
'''

from com.driver.zdns_driver import dns_zone_driver


class DnsRrsController(object):

    def __init__(self):
        # self.manager = dns_zone_driver.get_instance()
        self.manager = dns_zone_driver()


    def index(self):
        return {"Information": "The url is for DNS Acl RestApi "
                "interface"}

    '''
    get the list of rrs of zdns_driver
    http://ip:port/v3/dns/rrs/list?view_id=123&zone_id=123
    '''
    def list(self, **args):
        if args.get('view_id',-1) or args.get('zone_id',-1):
            view_id=args.get('view_id')
            zone_id=args.get('zone_id')
        else:
            return {
                'error':'400',
                'message':'view_id or zone_id is inqure'
                }

        # LOG.info(_("get the all of rrs of dns from zdns_driver,view_id is %(view_id)s"), {"view_id": view_id})

        # get the all of rrs 
        rrs = self.manager.get_rrs_driver(view_id,zone_id)
        # LOG.info(_("get the all of rrs of dns from zdns_driver done,response is %(rrs)s"), {"rrs": rrs})
        return rrs
