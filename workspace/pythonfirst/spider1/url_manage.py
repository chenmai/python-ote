'''
Created on 2016年6月1日

@author: hasee
'''

urlall=[]

# 检查url是否存在于url池
def ishad(url):
    if url in urlall:
        return True
    else:
        urlall.append(url) 
        return False



    