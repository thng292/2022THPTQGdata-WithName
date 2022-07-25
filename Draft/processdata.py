import csv

raw = open("raw.txt",mode="r",encoding="utf-8")
#pre-processing
raw = raw.read()
raw = raw.replace(u"Toán:","toan")
raw = raw.replace(u"Ngữ,văn:","ngu-van")
raw = raw.replace(u"Vật,lí:","vat-li")
raw = raw.replace(u"Hóa,học:","hoa-hoc")
raw = raw.replace(u"Sinh,học:","sinh-hoc")
raw = raw.replace(u"Tiếng,Anh:","ngoai-ngu")
raw = raw.replace(u"Tiếng,Nga:","ngoai-ngu")
raw = raw.replace(u"Tiếng,Pháp:","ngoai-ngu")
raw = raw.replace(u"Tiếng,Trung:","ngoai-ngu")
raw = raw.replace(u"Tiếng,Nhật:","ngoai-ngu")
raw = raw.replace(u"Tiếng,Hàn:","ngoai-ngu")
raw = raw.replace(u"Tiếng,Đức:","ngoai-ngu")
raw = raw.replace(u"Lịch,sử:","lich-su")
raw = raw.replace(u"Địa,lí:","dia-li")
raw = raw.replace(u"GDCD:","gdcd")
raw = raw.replace(u"KHTN:","khtn")
raw = raw.replace(u"KHXH:","khxh")
raw = raw.split('\n')
head = ["sbd", "ten", "toan", "ngu-van", "ngoai-ngu", "vat-li", 
"hoa-hoc", "sinh-hoc", "khtn", "lich-su", "dia-li", "gdcd", "khxh"]

proed = []

for row in raw :
    data = row.split(',')
    # print(data)
    try :
        temp = {}
        temp['sbd'] = data[0]
        temp['ten'] = data[1]
        temp['toan'] = ""
        temp['ngu-van'] = ""
        temp['ngoai-ngu'] = ""
        temp['vat-li'] = ""
        temp['hoa-hoc'] = ""
        temp['sinh-hoc'] = ""
        temp['lich-su'] = ""
        temp['gdcd'] = ""
        temp['dia-li'] = ""
        temp['khtn'] = ""
        temp['khxh'] = ""
    except:
        print(row)
    for i in range(2,len(data),2) :
        temp[data[i]]=data[i+1]
    proed.append(temp)

# print(proed)
with open('raw.csv',mode='w',encoding='utf-8',newline='\n') as outf :
    out = csv.DictWriter(outf, fieldnames=head)
    out.writeheader()
    out.writerows(proed)