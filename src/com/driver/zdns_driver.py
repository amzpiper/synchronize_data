#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:guoyuhang

import logging
import requests
import time
import json
from com.config.config import Config


# 单例对象
DNS_DRIVER = None

class dns_zone_driver():

    def __init__(self):
        self.config = Config()
        self.host = 'https://' + self.config.host_ip
        self.port = self.config.port
        self.view_id = self.config.view_id
        self.auth_name = self.config.auth_name
        self.auth_pw = self.config.auth_pw

    @classmethod
    def get_instance(cls):
        global DNS_DRIVER
        if not DNS_DRIVER:
            DNS_DRIVER = cls()
        return DNS_DRIVER

    """   check_network     """
    def check_network(self):
        url = self.config.check_network_url
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(params)
        print("check_network :" + url)

        try:
            response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
            print("response.text: %s" % response.text)
            json.loads(response.text)
        except Exception as e:
            print("e.message:",e)
            response = {
                "error":500
            }
            return response
            
        # No JSON object could be decoded
        return json.loads(response.text)

    """   view all acls     """
    def get_acls_driver(self):
        url = (self.host + ":" + str(self.port) + '/acls')
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        auth = (self.auth_name, self.auth_pw)
        params = {'current_user': 'admin'}
        data = json.dumps(params)
        print("request all acls :" + url)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                print("response.text: %s" % response.text)
                json.loads(response.text)

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                    "total_size":8,
                    "page_num":1,
                    "page_size":8,
                    "resources":[
                        {
                            "id":"old_test_acls_name_1",
                            "name":"old_test_acls_name_1",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_1",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_2",
                            "name":"old_test_acls_name_2",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_2",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_3",
                            "name":"old_test_acls_name_3",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_3",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_4",
                            "name":"old_test_acls_name_4",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_4",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_5",
                            "name":"old_test_acls_name_5",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_5",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_6",
                            "name":"old_test_acls_name_6",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_6",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_7",
                            "name":"old_test_acls_name_7",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_7",
                            "comment":""
                        },
                        {
                            "id":"old_test_acls_name_8",
                            "name":"old_test_acls_name_8",
                            "network_count":2,
                            "networks":[
                                "192.168.1.0/24",
                                "192.168.2.0/24"
                            ],
                            "href":"/acls/old_test_acls_name_8",
                            "comment":""
                        },
                    ]
                }
                # time.sleep(3)
                # response = {
                #     "error":"null"
                # }
                return response
        except Exception as e:
            print("e.message:",e)
            response = {
                "error":500
            }
            return response

        return json.loads(response.text)

    """   view one acls     """
    def get_acl_one_driver(self,id):
        url = (self.host + ":" + str(self.port) + '/acls/' + id)
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)
        print("request one of acls :" + url)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                response = response.text

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                    "id":"old_test_acls_name_1",
                    "name":"old_test_acls_name_1",
                    "network_count":2,
                    "networks":[
                        "192.168.1.0/24",
                        "192.168.2.0/24"
                    ],
                    "href":"/acls/old_test_acls_name_1",
                    "comment":""
                }
                time.sleep(3)
                return response
        except Exception as e:
            response = {
                "error":500
            }
            return response

        return json.loads(response)

    """   view all views     """
    def get_views_driver(self):
        url = (self.host + ":" + str(self.port) + '/views')
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        auth = (self.auth_name, self.auth_pw)
        params = {'current_user': 'admin'}
        data = json.dumps(params)
        print("request all views :" + url)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                print("response: %s" % response.text)
                json.loads(response.text)

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                    "total_size":3,
                    "page_num":1,
                    "page_size":3,
                    "resources":[
                        {
                            "id": "test_view_name_1",
                            "name": "test_view_name_1",
                            "priority": "1",
                            "acls": [
                                "old_test_acls_name_1",
                                "old_test_acls_name_2"
                            ],
                            "href": "/views/test_view_name_1",
                            "owners": [
                                "local.master",
                                "local.slave"
                            ],
                            "dns64s": [],
                            "fail_forwarder": "",
                            "query_source": "",
                            "zones": [
                                {
                                    "master":[],
                                    "id":"oldv61.org"
                                },
                                {
                                    "master":[],
                                    "id":"oldv61.org"
                                }
                            ],
                            "comment": ""
                        },
                        {
                            "id": "test_view_name_2",
                            "name": "test_view_name_2",
                            "priority": "1",
                            "acls": [
                                "old_test_acls_name_1",
                                "old_test_acls_name_2"
                            ],
                            "href": "/views/test_view_name_2",
                            "owners": [
                                "local.master",
                                "local.slave"
                            ],
                            "dns64s": [],
                            "fail_forwarder": "",
                            "query_source": "",
                            "zones": [
                                {
                                    "master":[],
                                    "id":"oldv71.org"
                                },
                                {
                                    "master":[],
                                    "id":"oldv71.org"
                                }
                            ],
                            "comment": ""
                        },
                        {
                            "id": "test_view_name_3",
                            "name": "test_view_name_3",
                            "priority": "1",
                            "acls": [
                                "old_test_acls_name_1",
                                "old_test_acls_name_2"
                            ],
                            "href": "/views/test_view_name_3",
                            "owners": [
                                "local.master",
                                "local.slave"
                            ],
                            "dns64s": [],
                            "fail_forwarder": "",
                            "query_source": "",
                            "zones": [
                                {
                                    "master":[],
                                    "id":"oldv81.org"
                                },
                                {
                                    "master":[],
                                    "id":"oldv81.org"
                                }
                            ],
                            "comment": ""
                        },
                    ]
                }
                # time.sleep(3)
                return response
        except Exception as e:
            print("e.message:",e)
            response = {
                "error":500
            }
            return response

        return json.loads(response.text)

    """   view one views     """
    def get_view_one_driver(self,id):
        url = (self.host + ":" + str(self.port) + '/views/' + id)
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)
        print("one of view :" + url)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                response = response.text

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                    "id":"old_test_acls_name_1",
                    "name":"old_test_acls_name_1",
                    "network_count":2,
                    "networks":[
                        "192.168.1.0/24",
                        "192.168.2.0/24"
                    ],
                    "href":"/acls/old_test_acls_name_1",
                    "comment":""
                }
                time.sleep(3)
                return response
        except Exception as e:
            response = {
                "error":500
            }
            return response

        return json.loads(response)

    """   view all zone     """
    def get_zones_driver(self, view_id=None):
        if view_id:
            self.view_id = view_id
        else:
            self.view_id = self.view_id
        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones')

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        auth = (self.auth_name, self.auth_pw)
        params = {'current_user': 'admin'}
        data = json.dumps(params)
        print("request all zone :" + url)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                print("response.text: %s" % response.text)
                json.loads(response.text)

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                    "total_size":8,
                    "page_num":1,
                    "page_size":8,
                    "resources":[
                        {
                            "id":    "oldv6.org",
                            "name":   "oldv6.org",
                            "rrs":   {
                                "count":9,
                                "href":"/views/test_view_name_3/zones/oldv6.org/rrs"
                            },
                            "default_ttl":  7200,
                            "ad_controller": [],
                            "renewal":   "yes",
                            "owners":   ["local.master","local.slave"],
                            "comment":   "",
                            "masters":   [],
                            "slaves":   [],
                        },
                    ]
                }
                # time.sleep(3)
                return response
        except Exception as e:
            print("e.message:",e)
            response = {
                "error":500
            }
            return response

        return json.loads(response.text)

    """   view one zone     """
    def get_zone_one_driver(self, view_id, zone_id):
        if view_id:
            self.view_id = view_id
        else:
            self.view_id = self.view_id
        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones/' + zone_id)
        data = {}
        data["current_user"] = 'admin'
        data["need_zone_content"] = 'yes'
        data = json.dumps(data)
        auth = (self.auth_name, self.auth_pw)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        print("request one zone :" + url)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                response = response.text

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                }
                # time.sleep(3)
                return response
        except Exception as e:
            response = {
                "error":500
            }
            return response

        return json.loads(response)

    """   view all rrs     """
    def get_rrs_driver(self,view_id, zone_id):
        if view_id:
            self.view_id = view_id
        else:
            self.view_id = self.view_id
        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones/' + zone_id + "/rrs")
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        auth = (self.auth_name, self.auth_pw)
        params = {'current_user': 'admin'}
        data = json.dumps(params)
        print("request all rrs :" + url)

        try:
            if self.config.profile == "prop":
                response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
                print("response.text: %s" % response.text)
                json.loads(response.text)

            elif self.config.profile == "test":
                # 模拟数据
                response = {
                    "total_size":8,
                    "page_num":1,
                    "page_size":8,
                    "resources":[
                        {
                            "id": "ns.oldv6.org.$*******",
                            "name": "ns.oldv6.org.", 
                            "type": "NS",
                            "ttl": 7200,
                            "rdata": "127.0.0.1",
                            "klass": "IN",
                            "href": "/views/test_view_name_3/zones/oldv6.org/rrs/ns.oldv6.org.$*******"
                        },
                        {
                            "id": "a.oldv6.org.$*******",
                            "name": "a.oldv6.org.", 
                            "type": "A",
                            "ttl": 7200,
                            "rdata": "127.0.0.1",
                            "klass": "IN",
                            "href": "/views/test_view_name_3/zones/oldv6.org/rrs/ns.oldv6.org.$*******"
                        },
                    ]
                }
                # time.sleep(3)
                return response
        except Exception as e:
            print("e.message:",e)
            response = {
                "error":500
            }
            return response

        return json.loads(response.text)