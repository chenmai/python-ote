'''
Created on 2016年6月1日

@author: hasee
'''
from bs4 import BeautifulSoup
import urllib.request
import re


url_temp=[]

def explain(url):
    html_doc= urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc,"html5lib")
    links = soup.find_all('a',href=re.compile(r"/view/(.+?).htm"))
    for link in links:
        new_url = link['href']
        new_full_url= 'http://baike.baidu.com'+new_url
        url_temp.append(new_full_url)

def templist():
    return url_temp
#     返回一个url的列表
    