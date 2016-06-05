'''
Created on 2016年6月1日

@author: hasee
'''
from bs4 import BeautifulSoup
import re
html_doc ="""<html><head><title>The Dormouse's story</title></head><p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived at the bottom of a well.</p><p class="story">...</p>"""
soup = BeautifulSoup(html_doc,"html5lib")



soup.select("title")
print(soup.select("title"))
# [<title>The Dormouse's story</title>]

soup.select("p nth-of-type(3)")
print(soup.select("p nth-of-type(3)"))
# [<p class="story">...</p>]

soup.select("head > title")
# [<title>The Dormouse's story</title>]

soup.select("p > a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("p > a:nth-of-type(2)")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select("p > #link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("body > a")
# []