'''
Created on 2016年6月1日

@author: hasee
'''
from spider1 import url_manage
import urllib.request
from spider1.url_parser import explain, templist
from spider1.url_manage import urlalllist

rooturl='http://baike.baidu.com/view/21087.htm'

if url_manage.ishad(rooturl):
    pass
else:
    bank=[]
    explain(rooturl)
    bank=templist()
    banklength=len(bank)
    count=0
#     不能大于103
    while(count)<100:
        for i in bank:
            result=url_manage.ishad(i)
            if result==False:
                count=count+1
#                 explain(i)
        bank=templist()
        
    print(count)
        
        
        
#     while(len(urlalllist()))<500:
#         for i in bank:
#             result=url_manage.ishad(i)
#             if result==False:
#                 explain(i)
#         bank=templist()
#         print(result)