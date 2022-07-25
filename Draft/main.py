import time
import requests
import queue
out = open("out.txt",mode='w')
ts=0
waiting = queue.Queue()
for i in range(1,10) :
    for k in range(1000,9999) :
        response = requests.get('https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2019/'+'0'+str(i*1000000+k)+ '.html')
        print('0'+str(i*1000000+k)+ ' '+str(response.status_code))
        a = str(response.content)
        start = a.find('<table')
        end = a.find('</table>')
        out+=('0'+str(i*1000000+k)+'\t'+a[start:end]+'\n')
        time.sleep(0.01)
        if response.status_code != 200 :
            waiting.put('0'+str(i*1000000+k))

while len(waiting)!=0 :
  t = waiting.get()
  response = requests.get(f'https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/{t}.html')
  print(t + ' '+str(response.status_code))
  ts+=1
  a = str(response.content)
  start = a.find('<table')
  end = a.find('</table>')
  out+=(str(t) + '\t' + a[start:end]+'\n')
  time.sleep(0.01)
  if response.status_code != 200 :
      waiting.put('0'+str(i*1000000+k))

outf.write(out)
outf.close()
