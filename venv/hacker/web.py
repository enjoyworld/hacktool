#web 编程
import json

import requests
import  sys
url='https://www.ichunqiu.com/courses/ajaxCourses'
headers={
'Host': 'www.ichunqiu.com',
'Cookie': 'ci_session=5556dc2e440ce96873ca83d2ef0cd55ae41a2cae; chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; __jsluid_s=0cf0e28f6fc16d6865a881c029fe333c; UM_distinctid=17a2e04cb739-0215aaff642c248-4c3f2d73-144000-17a2e04cb7480e; CNZZDATA1262179648=517112684-1624266342-%7C1624266342; Hm_lvt_2d0601bd28de7d49818249cf35d95943=1624269705; Hm_lpvt_2d0601bd28de7d49818249cf35d95943=1624270932',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
data={'ageIndex':'1'}
r=requests.post(url=url,headers=headers,data=data)
datas=json.loads(r.text)
print(datas)