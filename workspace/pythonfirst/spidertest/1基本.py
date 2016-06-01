'''
Created on 2016年5月31日

@author: hasee
'''
import urllib.request

#返回请求（不懂）
response = urllib.request.urlopen('http://www.baidu.com/')

#读取整个网页（有些不对）
html = response.read()
print(html)