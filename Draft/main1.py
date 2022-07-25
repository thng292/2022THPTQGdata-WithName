import requests
import json

out = open('out.csv', mode='w')

for i in range(1,10) :
    for j in range(0,10) :
        for k in range(1000,9999) :
            code = '0'+str(i)+'0'+str(j)+str(k)
            data = dict(json.loads(str(requests.post('https://diemthi.vnanet.vn/Home/SearchBySobaodanhFile',json={'code':code, 'nam': 2022}).text)))
            if data['message'] == 'success' and data['result'] :
                print(code)
                data = data["result"][0]
                out.write(str(data['Toan'])+','+str(data['NguVan'])+','+str(data['NgoaiNgu'])+','+str(data['VatLi'])+','+str(data['HoaHoc'])+','+str(data['SinhHoc'])+','+str(data['LichSu'])+','+str(data['DiaLi'])+','+str(data['GDCD'])+'\n')

out.close()