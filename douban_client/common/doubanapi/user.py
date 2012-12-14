#/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jiangyt'

import httplib
from urllib import urlencode
import json

class User(object):

    apiurl = ''

    def __init__(self, apiurl = 'api.douban.com'):
        self.apiurl = apiurl

    def __repr__(self):
       return '======DouBan User API called======'

    @property
    def me(self):
        return self.get('~me')

    "get user infos by user_id"
    def get(self, id):
        
        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {}

            if (id == "~me"):
                token = raw_input("input the token of yours ==>>")
                headers = {
                        'Authorization': "Bearer %s" % token
                        }

            conn.request('GET', '/v2/user/' + id, headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "get user info raised exception reason ==>> %s" % e

    def query_user(self, q, start, count):

        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {}

            params = {
                    'q': q,
                    'start': start,
                    'count': count
                    }

            conn.request('GET', '/v2/user/search', body = urlencode(params), headers = headers)
            response = conn.getresponse()
            data = response.read()
            #data = json.loads(data, ensure_ascii = False)

            #return data.decode('unicode-escape').encode('utf-8')
            return data
        except Exception , e:
            print "get user info raised exception reason ==>> %s" % e
            
if __name__ == "__main__":

    user = User()
    print user.me
    #print user.get('cnny-leon')
    print user.query_user('cnny-leon', 0, 100)
