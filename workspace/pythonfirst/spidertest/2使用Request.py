'''
Created on 2016年5月31日

@author: hasee
'''
import urllib.request

#使用请求 不懂
req = urllib.request.Request('http://www.baidu.com/')

# 不懂
response = urllib.request.urlopen(req)

# 读取网页
the_page = response.read()

# print(the_page)