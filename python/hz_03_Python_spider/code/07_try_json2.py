import requests
from  retrying import *
import json

url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1534255320421"

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36","Referer": "https://m.douban.com/tv/american"}

response = requests.get(url,headers=headers)
json_str = response.content.decode()
print(type(json_str))
ret1 = json.loads(json_str)
#print(ret1)
print(type(ret1))

with open("01_douban.html","w") as d:
    d.write(json.dumps(ret1,ensure_ascii=False,indent=2))
#print(type(json_str))
#print(json_str)  