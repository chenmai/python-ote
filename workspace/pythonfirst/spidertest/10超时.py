'''
Created on 2016年5月31日

@author: hasee
'''
import socket
import urllib.request

# timeout in seconds
timeout = 2
socket.setdefaulttimeout(timeout)

# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.111cn.net /')
a = urllib.request.urlopen(req).read()
print(a)