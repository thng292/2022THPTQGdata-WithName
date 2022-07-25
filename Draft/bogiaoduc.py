from operator import mod
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import csv

url = "https://diemthi.hcm.edu.vn/Home/Show"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

a = u"Toán:"
rows = []
#02071272
for k in range(0,99999) :
    sbd = f"SoBaoDanh=0{2000000+k}"
    print(sbd) 
    resp = requests.post(url, headers=headers, data=sbd)
    data = BeautifulSoup(str(resp.text), 'html.parser')
    #print(data)
    try :
        data = list(data.table.get_text().split())
        data = data[7:]
    except :
        continue
    ten = ''
    for i,j in enumerate(data):
        if j==a :
            temp = data[i:]
            temp.insert(0,ten)
            temp.insert(0,sbd[10:])
            rows.append(temp)
            print(ten)
            break
        ten+=(j+' ')
with open('out.csv', 'w',encoding='utf-8') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the data rows 
    csvwriter.writerows(rows)