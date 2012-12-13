#!/usr/bin/python

# - *-coding: utf-8-*-

__author__='jiangyt'

import httplib
from  urllib import urlencode

def getAccess(type, code):
    url = "www.douban.com"
    port = 443
    method_params = ''

    if type == "_code_":
        params = {
                'client_id' : '00ee4649c62b9d6302cad2dd5282d829',
                'client_secret' : 'b6a45d07d205cd14',
                'redirect_uri' : 'http://site.douban.com/196738/',
                'grant_type' : 'authorization_code',
                'code' : code
                }
    else:
        params = {
                'client_id' : '00ee4649c62b9d6302cad2dd5282d829',
                'client_secret' : 'b6a45d07d205cd14',
                'redirect_uri' : 'http://site.douban.com/196738/',
                'grant_type' : 'authorization_code',
                'refresh_token' : code
                }


    headers = {"Content-Type" : "application/x-www-form-urlencoded"}

    data = ""

    try:
        conn = httplib.HTTPSConnection(url, port)
        conn.request("POST", "/service/auth2/token", body = urlencode(params), headers = headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception ,e:
        print "Error ocurred:==>>%s" % e 

    return data

if __name__ == "__main__":

    code = raw_input("input the authorization_code >>")
    print getAccess('_code_', code)
