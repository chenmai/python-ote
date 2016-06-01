'''
Created on 2016年5月31日

@author: hasee
'''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request("http://www.111cn.net /")
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print("good!")
    print(response.read().decode("utf8"))