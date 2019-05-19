import requests
from retrying import *

#url = "http://fanyi.baidu.com"
url = "http://www.google.com"
query_sting = {"query":"人生苦短，我用Python","from":"zh","to":"en"}

#headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Mobile Safari/537.36"}
headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}

response = requests.post(url,data=query_sting,timeout=2)

# 获取网页的HTML字符串
#response.encoding = "utf-8"
#print(response.text)  # 使用.text 容易乱码，需要制定 UTF-8 编码
try:
    print(response.content.decode())
except Exception as result:
    print("Erro:%s" % result)

 