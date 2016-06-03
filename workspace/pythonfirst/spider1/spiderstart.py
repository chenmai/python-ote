'''
Created on 2016年6月3日
爬虫启动程序
@author: Administrator
'''
from spider1.url_manage import check_new_url, get_url_seed, url_seed_to_hadused,\
    length_url_hadused, length_url_seed
from spider1.url_parser import explain, get_new_urllist

def spiderstart(url):
    a=check_new_url(url)
#     检查url是否被使用
    count=0
#     爬取次数
    while count<10:
        if a==0:
            temp0=url_seed_to_hadused()
#             把url放入已爬取的url列表中
            temp1,now_url=explain(temp0)
#             url没有用过，就解析这个url
            temp2=get_new_urllist(temp1)
#             解析完全，返回新的url列表temp2
            temp3=len(temp2)
#             得知新的url列表有几个url
            print(now_url,'上爬取页面完成')
            for i in range(temp3):
                if check_new_url(temp2[i])==1:
                    continue
                
#                 print(temp2[i])
                
            get_url_seed()
#             添加完成后,获取新的待爬取列表    
            count=count+1
#             计数加1  
        else:
            print('url已经被记录使用，启动失败')
    print('当前待爬取列表中的url个数=',length_url_seed())
#     显示当前待爬取列表中的url个数
    print('已爬取的url个数    =',length_url_hadused())
#     显示已爬取的url个数        
    