'''
Created on 2016年6月1日

@author: hasee
'''

urlall=[]


# 检查url是否存在于url池
def ishad(url):
    if url in urlall:
#         True代表存在
        print('已经存在的网址')
        return True
    else:
        urlall.append(url) 
#         False代表不存在，已添加
        print('不在url池，现在已添加,url=',url)
        return False

def urlalllist():
    return urlall        




    