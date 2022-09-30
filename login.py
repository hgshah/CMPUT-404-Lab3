# reference taken from https://github.com/aianta/cgi-lab/blob/master/login.py : TA Alex
#!/usr/bin/env python3

import cgi
import os
from templates import login_page
from templates import secret_page

dict = {}
for x in dict:
    if x is None:
        del dict[x]
    else:
       dict.update(os.environ)


cookies = dict
print(cookies)

#cookies = parse_cookies(os.environ["HTTP_COOKIE"])

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

header = ""
header += "Content-Type: text/html\r\n"    # HTML is following

body = ""

if username is not None or ('logged' in cookies and cookies['logged'] == "true"):
#if username is not None:
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    #header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>Dont share with anyone</h1>"
else:
    body += login_page()

print(header)
print()
print(body)