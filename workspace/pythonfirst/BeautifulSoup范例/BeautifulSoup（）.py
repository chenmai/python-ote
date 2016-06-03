'''
Created on 2016年6月1日

@author: hasee
'''

from bs4 import BeautifulSoup
import re




html_doc ="""<html><head><title>The Dormouse's story</title></head><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p>"""
soup = BeautifulSoup(html_doc,"html5lib")
# content = urllib.request.urlopen('http://baike.baidu.com/view/21087.htm').read()
# html=BeautifulSoup(content,"html.parser")
# 
# print(html)

print(soup.find_all('b'))
# 搜索节点b,返回列表
# [<b>The Dormouse's story</b>]

soup.find_all("title")
print(soup.find_all("title"))
# 搜索name=title的tag
# [<title>The Dormouse's story</title>]

soup.find_all(id="link2")
print(soup.find_all(id="link2"))
# 搜索名为id属性的tag，然后筛选name
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.find_all(href=re.compile("elsie"))
print(soup.find_all(href=re.compile("elsie")))
# 搜索href参数，正则提取全部,列表输出
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.find_all(id=True)
print(soup.find_all(id=True))
# 搜索所有带属性带id的tag
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>',"html5lib")
data_soup.find_all(attrs={"data-foo": "value"})
print(data_soup.find_all(attrs={"data-foo": "value"}))
# 自定义属性搜索
# [<div data-foo="value">foo!</div>]









# CCS方法



soup.find_all("a", class_="sister")
print(soup.find_all("a", class_="sister"))
# CCS类名搜索,用class_
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(class_=re.compile("itl"))
# CCS正则
# [<p class="title"><b>The Dormouse's story</b></p>]

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
soup.find_all(class_=has_six_characters)
# 定义方法来CCS
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

css_soup = BeautifulSoup('<p class="body strikeout"></p>',"html5lib")
css_soup.find_all("p", class_="strikeout")
# 局部搜索
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# 局部搜索
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body strikeout")
# 完整搜索
# [<p class="body strikeout"></p>]





# CSS选择器





# Text参数
soup.find_all(text="Elsie")
print(soup.find_all(text="Elsie"))
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
print(soup.find_all(text=re.compile("Dormouse")))
# [u"The Dormouse's story", u"The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    ""'Return True if this string is the only child of its parent tag.'""
    return (s == s.parent.string)
soup.find_all(text=is_the_only_string_within_a_tag)
print(soup.find_all(text=is_the_only_string_within_a_tag))
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']


# 限制返回数量
soup.find_all("a", limit=2)
print(soup.find_all("a", limit=2))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]











for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
#     正则搜索
# body
# b

soup.find_all(["a", "b"])
print(soup.find_all(["a", "b"]))
# 列表返回a节点,b节点
# [<b>The Dormouse's story</b>, <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for tag in soup.find_all(True):
    print(tag.name)
#     显示所有tag名,但是不会返回字符串节点
#     html
#     head
#     title
#     body
#     p
#     b
#     p
#     a
#     a
#     a
#     p



print(soup)
# 解析后文档
# <html><head><title>The Dormouse's story</title></head><body><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p></body></html>


soup.head
# 文档头
print(soup.head)
# <head><title>The Dormouse's story</title></head>

head_tag = soup.head
# 节点的处理，如head部分


head_tag.contents
# head部分的下个节点,列表形式
print(head_tag.contents)
# [<title>The Dormouse's story</title>]


len(list(soup.children))
# 查看子属性个数
print(len(list(soup.children)))
# 1
len(list(soup.descendants))
print(len(list(soup.descendants)))
# 25


for child in head_tag.descendants:
    print(child)
    # descendants方法打印该属性
    # <title>The Dormouse's story</title>
    # The Dormouse's story


title_tag = head_tag.contents[0]
print(title_tag)
# 从提取的里面读取字符串
# <title>The Dormouse's story</title>


print(title_tag.string)
# 单个tag

print(soup.html.string)
# 多个tag会None

for string in soup.strings:
    print(repr(string))
    # 循环方法打印全部tag

for string in soup.stripped_strings:
    print(repr(string))
    # 等效（去空格）
#     "The Dormouse's story"
#     "The Dormouse's story"
#     'Once upon a time there were three little sisters; and their names were'
#     'Elsie'
#     ','
#     'Lacie'
#     ' and'
#     'Tillie'
#     ';and they lived at the bottom of a well.'
#     '...'



for child in title_tag.children:
    print(child)
    # children方法打印title_tag的所有子标签
    # The Dormouse's story

title_tag.contents
print(title_tag.contents)
# 提取的标题中去掉<title></title>,列表显示
# ["The Dormouse's story"]


text = title_tag.contents[0]
print(text)
# 列表第一个值
# The Dormouse's story


print(soup.contents)
# 解析后文档内容
# [<html><head><title>The Dormouse's story</title></head><body><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p></body></html>]


print(len(soup.contents))
# 解析后文档内容长度1
# 1


print(soup.contents[0].name)
# 解析后文档内容的名称
# html


# 父节点方法
title_tag = soup.title
print(title_tag)
# <title>The Dormouse's story</title>

title_tag.parent

print(title_tag.parent)
# <head><title>The Dormouse's story</title></head>
print(title_tag.parent.parent)
# <html><head><title>The Dormouse's story</title></head><body><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p></body></html>
print(title_tag.string.parent)
# <title>The Dormouse's story</title>
print(title_tag.string.parent.parent)
# <head><title>The Dormouse's story</title></head>
print(title_tag.string.parent.parent.parent)
# <html><head><title>The Dormouse's story</title></head><body><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p></body></html>
# 显示上一级






soup.body.b
print(soup.body.b)
# body下的<b>的中间部分
# <b>The Dormouse's story</b>


soup.a
print(soup.a)
# 获取第一个 a标签下的内容
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

link = soup.a
print(link.parent)
# 获取a标签的父节点
# <p class="story">Once upon a time there were three little sisters; and their names were<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;and they lived at the bottom of a well.</p>

for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
#         历遍父节点
#         p
#         body
#         html
#         [document]



soup.find_all('a')
print(soup.find_all('a'))
# 获得所有a标签的内容,列表返回
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 兄弟节点
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>","html5lib")
# 查看文档结构
print(sibling_soup.prettify())
# <html>
#  <head>
#  </head>
#  <body>
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>
#  </body>
# </html>

# 查看对于的兄弟节点
sibling_soup.b.next_sibling
print(sibling_soup.b.next_sibling)
# <c>text2</c>
sibling_soup.c.previous_sibling
print(sibling_soup.c.previous_sibling)
# <b>text1</b>

# 历遍所有的sibling
for sibling in soup.a.next_siblings:
    print(repr(sibling))
#     ','
#     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
#     ' and'
#     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
#     ';and they lived at the bottom of a well.'

# 历遍所有的previous_sibling
for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))
#     ' and'
#     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
#     ','
#     <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#     'Once upon a time there were three little sisters; and their names were'
