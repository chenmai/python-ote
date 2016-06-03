'''
Created on 2016年6月3日

@author: Administrator
'''
from spider1.url_parser import explain, get_new_urllist
from spider1.url_manage import ishad, urlseedist, get_seed_url, del_seed_url,\
    add_urlhadused


rooturl='http://baike.baidu.com/view/21087.htm'


links=explain(rooturl)
url_temp=get_new_urllist(links)
url_length=len(url_temp)
for i in range(url_length):
    ishad(url_temp[i])
while len(urlseedist())<1000:
    new_url=get_seed_url()
    links_temp=explain(new_url)
    url_new_temp=get_new_urllist(links_temp)
    url_new_length=len(url_new_temp)
    for j in range(url_new_length):
        if ishad(url_temp[j])==0:
            a=get_seed_url()[0]
            add_urlhadused(a)
            del_seed_url()
            print(a)
print(urlseedist())