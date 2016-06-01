'''
Created on 2016年6月1日

@author: hasee
'''
import urllib.request
from bs4 import BeautifulSoup


content = urllib.request.urlopen('http://baike.baidu.com/view/21087.htm').read()
html=BeautifulSoup(content,"html.parser")

print(html)