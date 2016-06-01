'''
Created on 2016年6月1日

@author: Administrator
'''
#coding=utf-8
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response)
buff = response.read()
# print(buff)
#转码后显示
html = buff.decode("utf8")
# print(html)
response.close()
