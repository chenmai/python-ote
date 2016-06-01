'''
Created on 2016年6月1日

@author: Administrator
'''
import urllib.parse
import urllib.request

url = 'http://test.haibei.com/api/member/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username' : '123456@163.com',
          'password' : 'aaa123' }
headers = { 'User-Agent' : user_agent }

data = urllib.parse.urlencode(values).encode(encoding='UTF8')
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)