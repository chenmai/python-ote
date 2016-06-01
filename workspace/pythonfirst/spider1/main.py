'''
Created on 2016年6月1日

@author: hasee
'''
from spider1 import url_manage
import urllib.request

url='http://www.baidu.com/'

if url_manage.ishad(url):
    pass
else:
    response = urllib.request.urlopen(url)
    html=response.read()#.decode("utf8")
    print(html)