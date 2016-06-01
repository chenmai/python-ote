'''
Created on 2016年5月30日

@author: hasee
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            
            fout.write("<td>%s</td>"% data['url'])
            fout.write("<td>%s</td>"% data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"% data['summary'])
            
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
    
        
        fout.close()
    
    
    
    



