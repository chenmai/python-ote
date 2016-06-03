'''
Created on 2016年6月1日

@author: hasee
'''
from spider1.url_parser import explain

urlseed=[]
urlhadused=[]


# 检查url是否存在于url池，在返回Ture，不在就返回False并添加至url池
def ishad(url):
    if (url in urlseed) or (url in urlhadused) :
#         True代表存在
#         print('已经存在的网址')
#         return 1
        pass
    else:
        urlseed.append(url) 
#         False代表不存在，已添加
#         print('不在url池，现在已添加,url=',url)
#         return 0


def urlseedist():
    return urlseed        
# 返回url池

def get_seed_url():
    return urlseed[0]
# 获取url池的第一个url

def del_seed_url():
    del urlseed[0]
    
# 删除url池的第一个url

def url_word(url):
    explain(url)
# url池工作流程    

def add_urlhadused(url):
    urlhadused.append(url)
# 添加url进已使用的url池

def get_urlhadused():
    return urlhadused
    