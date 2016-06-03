'''
Created on 2016年6月2日

@author: Administrator
'''

# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

import urllib.request
from bs4 import BeautifulSoup
from setuptools.compat import unicode

soup=BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")

# 修改html部分


# tag部分

tag=soup.b
type(tag)
tagtype=type(tag)
print('tagtype     ',tagtype)
# tagtype      <class 'bs4.element.Tag'>
# 1:获取tag为b的tag

tag['class'] = 'verybold'
tag['id'] = 1
print('tag     ',tag)
# tag      <b class="verybold" id="1">Extremely bold</b>
print('获取定义过的tagclass     ',tag.get('class'))
# 获取定义过的tagclass      verybold
# 2:修改tag里的class和id


del tag['class']
del tag['id']
print('删除tagclass后的tag     ',tag)
# 3:删除class和id
# 删除tagclass后的tag      <b>Extremely bold</b>


soup=BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag=soup.b
tag.string
print(tag.string)
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>
print(type(tag.string))
# 4:提取tag里面的字符串


unicode_string = unicode(tag.string)
print(unicode_string)
# u'Extremely bold'
type(unicode_string)
print(type(unicode_string))
# <class 'str'>
# 转码  从 <class 'bs4.element.NavigableString'>变为 <class 'str'>


soup=BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag=soup.b
# 修改tag内的字符串

tag.string.replace_with("No longer bold")
print(tag)
# tag.string.replace_with
# <b class="boldest">No longer bold</b>





# HTML5部分


css_soup = BeautifulSoup('<p class="body strikeout"></p>',"html5lib")
print('html5获取多个class，结果列表     ',css_soup.p['class'])
# 1:获取class，以列表形式输出
# css_soup.p['class']
# html5获取多个class，结果列表      ['body', 'strikeout']

css_soup = BeautifulSoup('<p class="body"></p>',"html5lib")
print('html5获取单个class，结果列表      ',css_soup.p['class'])
# html5获取单个class，结果列表       ['body']


id_soup = BeautifulSoup('<p id="my id"></p>',"html5lib")
print('获取id     ',id_soup.p['id'])
# 2:获取id（只有一个）
# id_soup.p['id']
# 获取id      my id


rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>',"html5lib")
print('查看其中一个属性,如\'rel\'     ',rel_soup.a['rel'])
# 3:查看其中一个属性
# rel_soup.a['rel']
# 查看其中一个属性,如'rel'      ['index']


rel_soup.a['rel'] = ['index', 'contents']
print('修改后重新查看     ',rel_soup.p)
# 4:修改一个属性如[rel],重新查看
# 修改后重新查看      <p>Back to the <a rel="index contents">homepage</a></p>




# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
# xml_soup.p['class']
# print(xml_soup.p['class'])
# u'body strikeout'
# 因为系统问题无法安装库   pip install lxml  Microsoft Visual C++ 10.0 is required (Unable to find vcvarsall.bat)
# 解决办法:下载安装VS2010  http://pan.baidu.com/share/link?shareid=1609273194&uk=3255422755
# 官网https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs










