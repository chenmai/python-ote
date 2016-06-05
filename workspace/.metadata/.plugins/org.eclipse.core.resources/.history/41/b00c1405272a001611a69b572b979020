'''
Created on 2016年6月1日

@author: hasee
'''
from bs4 import BeautifulSoup
import urllib.request
import re





def explain(url):
    now_url=url
    html_doc= urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc,"html5lib")
    links = soup.find_all('a',href=re.compile(r"/view/(.+?).htm"))
# 待会添加值一起返回
    return links,now_url
# 解析传入的url,从上面爬取新的网址,返回新网址    

def get_new_urllist(links):
    url_temp=[]
    for link in links:
        new_url = link['href']
        new_full_url= 'http://baike.baidu.com'+new_url
        url_temp.append(new_full_url)
    return url_temp
# 传入解析后的url，将其转化为url列表,返回


    