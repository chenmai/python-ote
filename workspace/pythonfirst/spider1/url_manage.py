'''
Created on 2016年6月1日

@author: hasee
'''
url_seed=[]
url_hadused=[]

def check_new_url(url):
    if (url in url_seed)or(url in url_hadused):
        return 1
    else:
        url_seed.append(url)
        return 0
# 检查url是否已经被记录

def checl_url_used(url):
    if url in url_hadused:
        return 1
    else:
        url_hadused.append(url)
        return 0
# 检查url是否已经被使用过

def url_seed_to_hadused():
    temp = url_seed[0]
    url_hadused.append(url_seed[0])
    del url_seed[0]
    return temp 
# 从把使用的url放入使用过的url池中,返回放入的值


def length_url_seed():
    return len(url_seed)
# 返回url_seed的列表长度

def length_url_hadused():
    return len(url_hadused)
# 返回url_hadused的列表长度

def get_url_seed():
    return url_seed
# 获取url_seed的url列表



