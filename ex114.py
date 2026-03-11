import urllib
import urllib.request

try: urllib.request.urlopen('http://www.google.com')
except:
    print('deu erro')
else:
    print('deu good')