'''
Created on 2016年6月1日

@author: Administrator
'''
import urllib.request
import urllib.parse
data = {}
data['username'] = '123456@163.com'
data['password'] = 'aaa123'
#data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)
# name='Somebody+Here&language\=Python&location\=Northampton'
url = 'http://test.haibei.com/api/member/login'
full_url = url + '?' + url_values
print(full_url)
data = urllib.request.urlopen(full_url)

print(data)

the_page = data.read()
print(the_page)
