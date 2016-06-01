'''
Created on 2016年6月1日

@author: hasee
'''
#!/usr/bin/env python
#-*-coding:utf-8-*-


from pip._vendor.six import unichr
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    #检索开头标签
    def handle_starttag(self,tag,attrs):
        print ("Start tag:",tag)
        #匹配里面的项
        for attr in attrs:
            print ("    attr:",attr)
    #匹配结束标签
    def handle_endtag(self,tag):
        print ("End tag  :",tag)
    #处理数据
    def handle_data(self,data):
        print ("Data     :",data)
    #检索注释内容
    def handle_comment(self,data):
        print ("Comment  :",data)
    #处理转义字符
    def handle_entityref(self,name):
        c = unichr(name2codepoint[name])
        print ("Named ent:",c)
    #处理转义的数字字符（ACSII）
    def handle_charref(self,name):
        if name.startswith('x'):
            c = unichr(int(name[1:],16))    #十六进制
        else:
            c = unichr(int(name))
        print ("Num ent  :",c)
    #匹配HTML头
    def handle_decl(self,data):
        print ("Decl     :",data)

parser = MyHTMLParser()

parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML4.01//EN"''"http://www.w3.org/TR/html4/strict.dtd">')
#Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML4.01//EN""http://www.w3.org/TR/html4/strict.dtd"

parser.feed('<img src="python-logo.png" alt="The Python logo">')
#Start tag: img
#    attr: ('src', 'python-logo.png')
#    attr: ('alt', 'The Python logo')

parser.feed('<style type="text/css">#python { color: green }</style>')
#Start tag: style
#    attr: ('type', 'text/css')
#Data     : #python { color: green }
#End tag  : style

parser.feed('<script type="text/javascript"> alert("<strong>hello!</strong>");</script>')
#Start tag: script
#    attr: ('type', 'text/javascript')
#Data     :  alert("<strong>hello!</strong>");
#End tag  : script

parser.feed('<!-- a comment --><!--[if IE 9]>IE-specific content<![endif]-->')
#Comment  :  a comment 
#Comment  : [if IE 9]>IE-specific content<![endif]

parser.feed('&gt;>&#x3E;')
#Named ent: >
#Num ent  : >
#Num ent  : >

parser.feed('<p><a class=link href=#main>tag soup</p ></a&#62;')
#Start tag: p
#Start tag: a
#    attr: ('class', 'link')
#    attr: ('href', '#main')
#Data     : tag soup
#End tag  : p
#End tag  : a