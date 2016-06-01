'''
Created on 2016年6月1日

@author: Administrator
'''
#coding=utf-8
import urllib.request

req = urllib.request.Request('http://www.baidu.com')
print(req)
response = urllib.request.urlopen(req)
buff = response.read()
print(buff)
# 显示
the_page = buff.decode("utf8")
response.close()
print(the_page)