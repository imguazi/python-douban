#s/usr/bin/env python
# -*-coding: utf-8-*-

__author__ = 'jiangyt'

import httplib
from urllib import urlencode

class Book(object):

    apiurl = ''
    apikey = ''

    def __init__(self, apiurl = 'api.douban.com', apikey = '00ee4649c62b9d6302cad2dd5282d829'):
        self.apikey = apikey
        self.apiurl = apiurl

    def __repr__(self):
       return '======DouBan Book API called======'

    "get book infos by book_id, and getting most marked tags by marked "
    def get(self, id, tags):
        
        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {}

            if (True == False):
                conn.request('GET', '/v2/book/' + id, headers = headers)
            else:
                conn.request('GET', '/v2/book/' + id + '/tags', headers = headers)

            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "get book info raised exception reason ==>> %s" % e

    "get book infos by book_isbn"
    def get_by_isbn(self, id):
        
        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {}

            conn.request('GET', '/v2/book/isbn/' + id, headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "get book info raised exception reason ==>> %s" % e

    def query_book(self, q, tag, start, count):

        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {
		    'Content-Type': 'application/x-www-form-urlencode'
		    }

            params = {
                    'q': q,
                    'tag': tag,
                    'start': start,
                    'count': count
                    }

            conn.request('GET', '/v2/book/search', body = urlencode(params), headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "get book info raised exception reason ==>> %s" % e

    def get_collections(self, user_id, status = '', tag = '', time_from = '', time_to = '', rating = '0'):

        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {
		    'Content-Type': 'application/x-www-form-urlencode',
		    }

            params = {
                    'apikey': self.apikey,
                    'tag': tag,
                    'from': time_from,
                    'to': time_to,
                    'rating': rating
                    }

            conn.request('GET', '/v2/book/user/' + user_id + '/collections', body = urlencode(params), headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "get user collections raised exception reason ==>> %s" % e


    # 获取用户对某本图书的收藏信息
    def get_collection(self, token, book_id):

        try:
            conn = httplib.HTTPSConnection(self.apiurl)
            headers = {
		    'Content-Type': "application/x-www-form-urlencode",
                    'Authorization': "Bearer %s" % token
		    }

            params = {
                    'apikey': self.apikey,
                    }

            conn.request('GET', '/v2/book/' + book_id + '/collection', body = urlencode(params), headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "get user's  collection  of a book raised exception reason ==>> %s" % e

    # post comment to a book
    # book 评论所针对的book id
    # title 评论头
    # content
    # rating range 1 to 5, otherwist without rating

    def post_comment(self, token, book_id, tittle, content, rating):

        if not book:
            print "parameter book_id required"
            return
        elif not tittle:
            print "parameter comment tittle required"
            return
        elif not content:
            print "parameter comment content required"
            return

        if not rating in range(1, 5):
            print "you rate for book is %s " % rating

        try:
            conn = httplib.HTTPSConnection(self.apiurl)


            headers = {
		    'Content-Type': 'application/x-www-form-urlencode',
                    'Authorization': "Bearer %s" % token
		    }

            params = {
                    'book_id': book_id,
                    'tittle': tittle,
                    'content': content,
                    'rating': rating,
                    }

            conn.request('POST', '/v2/book/reviews', body = urlencode(params), headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data
        except Exception , e:
            print "post review raised exception reason ==>> %s" % e

    # 收藏某本图书
    #
    # status (收藏状态      必填（想读：wish 在读：reading 读过：read）
    # tags 收藏标签字符串  选填，用空格分隔
    # comment 短评文本        选填，最多350字
    # privacy 隐私设置     选填，值为'private'为设置成仅自己可见，其他默认为公开
    # rating 星评  选填，数字1～5为合法值，其他信息默认为不评星

    def post_add_collection(self, token, book_id, status, tags = [], comment = '', privacy = 'public', rating = '5'):

        if not book_id:
            print "parameter book_id required"
            return

        if not status:
            print "parameter status required"
            return

        try:
            conn = httplib.HTTPSConnection(self.apiurl)

            headers = {
		    'Content-Type': 'application/x-www-form-urlencode',
                    'Authorization': "Bearer %s" % token
		    }

            params = {
                    'scope': 'book_basic_r, book_basic_w',
                    'book_id': book_id,
                    'tittle': tittle,
                    'content': content,
                    'rating': rating,
                    }

            conn.request('POST', '/v2/book/' + book_id + '/collection', body = urlencode(params), headers = headers)
            response = conn.getresponse()
            data = response.read()

            return data

        except Exception , e:
            print "post add book raised exception reason ==>> %s" % e

if __name__ == "__main__":

    book_id = '6021440'
    tittle = '评论很好'
    content = '这本书的评价很好，有空的时候去读读'
    rating = 2
    token = '5e299b864ae547f91a7cd292e0afd7eb'
    status = 'wish'

    book = Book()

    #print book.post_add_collection(token, book_id, status)
    print book.post_comment(token, book_id, tittle, content, rating)#unpassed
    #print book.get_collections(user_id = 'jiangyitao')
    #token = raw_input("input the token of yours ==>>")
    #print book.get_collection(token, book_id)

    #print book.get(book_id, tags=True)
    #print book.get_by_isbn('9787540453190')
    #print book.query_book('Thinking, Fast and Slow', [], 0, 10)
