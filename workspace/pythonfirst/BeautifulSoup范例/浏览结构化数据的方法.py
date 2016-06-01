'''
Created on 2016年6月1日

@author: hasee
'''
import urllib.request
from bs4 import BeautifulSoup

content = urllib.request.urlopen('http://baike.baidu.com/view/21087.htm').read()
html=BeautifulSoup(content,"html.parser")

title=html.title
print('解析获得的title=',title)

titlename=html.title.name
print('解析获得的titlename=',titlename)

titlestring=html.title.string
print('解析获得的titlestring=',titlestring)

titleparentname=html.title.parent.name
print('解析获得的titleparentname=',titleparentname)