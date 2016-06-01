'''
Created on 2016年5月31日

@author: hasee
'''
from urllib.request import Request, urlopen
from urllib.error import  URLError
req = Request("http://www.111cn.net /")
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\t fulfill the request.')
        print('Error code: ', e.code)
else:
    print("good!")
    print(response.read().decode("utf8"))