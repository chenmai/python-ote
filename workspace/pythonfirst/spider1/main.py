'''
Created on 2016年6月1日

@author: hasee
'''
from spider1.url_parser import explain, get_new_urllist
from spider1.url_manage import ishad
rooturl='http://baike.baidu.com/view/21087.htm'


links=explain(rooturl)
url_temp=get_new_urllist(links)
url_length=len(url_temp)
for i in range(url_length):
    ishad(url_temp[i])