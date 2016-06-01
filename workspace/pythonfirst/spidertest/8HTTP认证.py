'''
Created on 2016年5月31日

@author: hasee
'''
import urllib.request

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "https://www.111cn.net /"
password_mgr.add_password(None, top_level_url, 'rekfan', 'xxxxxx')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
a_url = "https://www.111cn.net /"
x = opener.open(a_url)
print(x.read())

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

a = urllib.request.urlopen(a_url).read().decode('utf8')
print(a)