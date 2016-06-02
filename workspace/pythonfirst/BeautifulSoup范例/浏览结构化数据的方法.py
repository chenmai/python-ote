'''
Created on 2016年6月1日

@author: hasee
'''
import urllib.request
from bs4 import BeautifulSoup
from bs4.element import CData

content = urllib.request.urlopen('http://baike.baidu.com/view/21087.htm').read()
soup=BeautifulSoup(content,"html.parser")


title=soup.title
print('解析获得的title=',title)
# 解析获得的title= <title>Python_百度百科</title>

titlename=soup.title.name
print('解析获得的titlename=',titlename)
# 解析获得的titlename= title


titlestring=soup.title.string
print('解析获得的titlestring=',titlestring)
# 解析获得的titlestring= Python_百度百科

titleparentname=soup.title.parent.name
print('解析获得的titleparentname=',titleparentname)
# 解析获得的titleparentname= meta

soup.name
print(soup.name)
# [document]


# 注释处理
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, "html5lib")

# 读取注释
comment = soup.b.string
print(comment)
# Hey, buddy. Want to buy a used parser?

# 注释重写（结合上面）
cdata = CData("A CDATA block")
comment.replace_with(cdata)
print(soup.b.prettify())
# <b>
#  <![CDATA[A CDATA block]]>
# </b>

# 转换注释类型
type(comment)
print(type(comment))
# <class 'bs4.element.Comment'>



# 格式化输出网页
print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>









