'''
Created on 2016年6月1日

@author: hasee
'''
from bs4 import BeautifulSoup
from setuptools.compat import unicode

soup=BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag=soup.b
tag.string.replace_with("No longer bold")
print(tag)
# tag.string
# print(tag.string)
# # u'Extremely bold'
# type(tag.string)
# # <class 'bs4.element.NavigableString'>
# print(type(tag.string))
# 
# unicode_string = unicode(tag.string)
# print(unicode_string)
# # u'Extremely bold'
# type(unicode_string)
# print(type(unicode_string))
