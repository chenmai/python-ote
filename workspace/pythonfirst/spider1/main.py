'''
Created on 2016年6月1日

@author: hasee
'''
from spider1.spiderstart import spiderstart


if __name__=="__main__":
    rooturl='http://baike.baidu.com/view/21087.htm'
    total=1
#     10次
    spiderstart(rooturl,total)