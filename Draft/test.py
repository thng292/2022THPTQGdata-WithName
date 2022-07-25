import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

inp = open('awfag.htm', mode='r',encoding='utf-8')

data = BeautifulSoup(inp.read(), 'html.parser')
try :
    data = list(data.tbody.get_text().split())[7:]
except :
    continue

a = u"Toán:"

for i,j in enumerate(data):
    if j==a :
        t = ''
        for k in data[i:] :
            t+=k+' '
        print(t)
        break
