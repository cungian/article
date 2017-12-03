# coding:utf8

import requests
import re

resp = requests.get('https://www.qiushibaike.com/')
with open('baike.html', 'w', encoding="utf-8") as f:
    f.write(resp.text)
duanzis = re.findall('<span>(.*?)</span>', resp.text, re.S)
for duanzi in duanzis:
    print(duanzi)
	
	
	
	#666677777888999555