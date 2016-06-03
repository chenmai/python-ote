'''
Created on 2016年6月3日

@author: Administrator
'''
import urllib.request
from bs4 import BeautifulSoup

url='http://baike.baidu.com/view/945740.htm'
html_doc= urllib.request.urlopen(url)
soup = BeautifulSoup(html_doc,"html5lib")
titlestring=soup.title.string
print('解析获得的titlestring=',titlestring)