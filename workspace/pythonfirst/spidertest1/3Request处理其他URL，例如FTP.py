'''
Created on 2016年6月1日

@author: Administrator
'''
#coding=utf-8
import urllib.request
req = urllib.request.Request('http://webftp.zzbaike.com/')
response = urllib.request.urlopen(req)
buff = response.read()
#显示
the_page = buff.decode("utf8")
response.close()
print(the_page)