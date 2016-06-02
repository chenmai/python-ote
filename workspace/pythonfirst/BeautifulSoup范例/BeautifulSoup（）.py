'''
Created on 2016年6月1日

@author: hasee
'''

from bs4 import BeautifulSoup


# content = urllib.request.urlopen('http://baike.baidu.com/view/21087.htm').read()
# html=BeautifulSoup(content,"html.parser")
# 
# print(html)

html_doc ="""<html><head><title>The Dormouse's story</title></head><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p>"""
soup = BeautifulSoup(html_doc,"html5lib")

# 整个文档
print(soup)
# <html><head><title>The Dormouse's story</title></head><body><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p></body></html>

# 文档头
soup.head
print(soup.head)
# <head><title>The Dormouse's story</title></head>

# 节点的处理，如head部分
head_tag = soup.head

# head部分的下个节点,列表形式
head_tag.contents
print(head_tag.contents)
# [<title>The Dormouse's story</title>]

# 从提取的里面读取字符串
title_tag = head_tag.contents[0]
print(title_tag)
# <title>The Dormouse's story</title>

# 提取的标题中去掉<title></title>,列表显示
title_tag.contents
print(title_tag.contents)

# body下的<b>的中间部分
soup.body.b
print(soup.body.b)
# <b>The Dormouse's story</b>

# 获取第一个 a标签下的内容
soup.a
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 获得所有a标签的内容,列表返回
soup.find_all('a')
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


