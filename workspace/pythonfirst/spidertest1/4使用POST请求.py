'''
Created on 2016年6月1日

@author: Administrator
'''
#coding=utf-8
import urllib.parse
# from urllib.request import Request
import urllib.request


url='http://test.haibei.com/api/member/login'
urllib.requesturl = 'http://test.haibei.com/api/member/login'
values = {'username' : '123456@163.com',
          'password' : 'aaa123'}
data = urllib.parse.urlencode(values).encode(encoding='UTF8')

req = urllib.request.Request(url, data)

response = urllib.request.urlopen(req)

print(response)

the_page = response.read()
print(the_page)