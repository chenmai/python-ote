'''
Created on 2016年6月1日

@author: hasee
'''

from sgmllib import SGMLParser
import urllib.request
 
class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_h4 = ""
        self.name = []
    def start_h4(self, attrs):
        self.is_h4 = 1
    def end_h4(self):
        self.is_h4 = ""
    def handle_data(self, text):
        if self.is_h4 == 1:
            self.name.append(text)
 
content = urllib.request.urlopen('http://list.taobao.com/browse/cat-0.htm').read()
listname = ListName()
listname.feed(content)
for item in listname.name:
    print (item.decode('gbk').encode('utf8'))