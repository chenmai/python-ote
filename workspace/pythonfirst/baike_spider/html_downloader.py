'''
Created on 2016年5月30日

@author: hasee
'''
import urllib


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()    
    



