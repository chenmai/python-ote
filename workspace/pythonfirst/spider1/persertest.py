'''
Created on 2016年6月2日

@author: hasee
'''
import urllib.request
from bs4 import BeautifulSoup
import re
url='http://baike.baidu.com/view/21087.htm'
html_doc= urllib.request.urlopen('http://baike.baidu.com/view/21087.htm')
soup = BeautifulSoup(html_doc,"html5lib")
 
links = soup.find_all('a',href=re.compile(r"/view/(.+?).htm"))
 
# print(links)
ab=0
for link in links:
    new_url = link['href']
#     结果/view/10812319.htm
    new_full_url= 'http://baike.baidu.com'+new_url
    ab=ab+1
    print(new_full_url)
#     结果http://baike.baidu.com/view/10812319.htm
print(ab)