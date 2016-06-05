'''
Created on 2016年6月4日

@author: hasee
'''

import mysql.connector;

# 打开数据库连接
db = mysql.connector.connect(host='localhost', port='3306', user='root', password="123456", database="test", use_unicode=True);

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
baidu1=4

# SQL 插入语句
sql = """INSERT INTO web(id,url,title)
         VALUES (null,"%s",'baidu2')"""%(baidu1)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()
    
    
