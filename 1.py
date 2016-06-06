import os
import re
os.chdir("D:\gongzuo\PICT")
fo = open("b.txt", "r+")
#print ("文件名为: ", fo.name)

line = fo.readlines()
#print ("读取第一行 %s" % (line))

a=len(line)

#print (a)
c=str(line)
print(c)


#
d=c.replace('\\t','","')
f=d.replace('\\n\'','"}')
g=f.replace('\'','\n{\"')
#h=g.replace('[','')
#i=h.replace(']','')
print(g)

fo.write(g)


# 关闭文件
fo.close()
