# 包导入
import requests
import json

url = "http://fanyi.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

#quer_str = input("输入内容：")
data = {"query":"德国","from":"zh","to":"en"}
print(data["query"])
response = requests.post(url,data=data,headers=headers,timeout=3)

dic = response.content.decode()
dict_ret = json.loads(dic)
print(type(dict_ret))
ret = dict_ret["trans"][0]["dst"]
print(ret)