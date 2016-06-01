'''
Created on 2016年5月31日

@author: hasee
'''
import urllib.request

req = urllib.request.Request('http://www.111cn.net ')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
print(e.read().decode("utf8"))