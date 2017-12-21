import urllib.parse
import urllib.request
import json
from time import sleep

'''read url file 
   get json data and write to file 
'''
url = 'http://localhost:8080/invest/right.action'

'''
values = {
'creditId' : 19815,
'pageIndex' : 2
}
'''

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
#page=urllib.request('https://sit.ibdp2p.com/invest/creditBidInfo.action?creditId=19566&pageIndex=2')

#读取数据标的编号及页码总数
sourceFile = open('data/right-info.txt', 'r')

count = 1719
for line in sourceFile:
    line = line.strip('\n')
    id = int(line.split(',')[0])
    totalPages = int(line.split(',')[1])

    print('开始处理:%s' %line)

    for i in range(1,totalPages+1):
        values = {
            'repaymentId': id,
            'pageIndex': i
        }

        data = urllib.parse.urlencode(values).encode(encoding='UTF8')
        req = urllib.request.Request(url,data,headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()
        #print(the_page.decode("utf8"))

        ddata=json.loads(the_page)
        #print('=========================================')
        #print(ddata['bidList'])

        filePath = 'data/json/rightInfo-%d-%d.json' %(id,i)
        try:
            file = open(filePath, 'w', encoding='utf-8')
            encode_json = json.dumps(ddata['rightinfoDetailList'])
            file.writelines(encode_json)
            #sleep(3)
        except Exception as msg:
            print(msg)
        finally:
            file.close()

    count -= 1
    print('还剩下未处理的标的数:%d' %count)
