'''
Date:2021/3/19
Author:Guoyha
'''

from com.driver.zdns_driver import dns_zone_driver


class ViewRequest(object):
    
    def __init__(self):
        # self.manager = dns_zone_driver.get_instance()
        self.manager = dns_zone_driver()
    
    def index(self):
        return {"Information": "The url is for DNS Views RestApi "
                "interface"}

    '''
    get the list of views of zdns_driver
    http://ip:port/v3/dns/views/list
    '''
    def list(self):
        # LOG.info(_("get the list of views of dns from zdns_driver"))

        # get the all of views 
        views = self.manager.get_views_driver()
        # LOG.info(_("get the list of views of dns from zdns_driver done,response is %(views)s"), {"views": views})    
        return views


    '''
    get the one of views of zdns_driver
    http://ip:port/v3/dns/views/show?view_id=:id
    '''
    def show(self, view_id):
        if str(view_id) == 0 :
            return {
                'error':'400',
                'message':'view_id or zone_id is inqure'
                }

        # LOG.info(_("get the one of views of dns from zdns_driver,view_id is %(view_id)s"), {"view_id": view_id})

        # get the one of views 
        views = self.manager.get_view_one_driver(view_id)
        # LOG.info(_("get the one of views of dns from zdns_driver done,response is %(views)s"), {"views": views})    
        return views