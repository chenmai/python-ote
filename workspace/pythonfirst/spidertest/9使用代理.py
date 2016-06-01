'''
Created on 2016年5月31日

@author: hasee
'''
import urllib.request

proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)


a = urllib.request.urlopen("http://www.111cn.net ").read().decode("utf8")
print(a)