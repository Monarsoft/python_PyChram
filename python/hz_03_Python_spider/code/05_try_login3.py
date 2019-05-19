import requests

#实例化session
session = requests.session()

post_url = "http://www.renren.com/PLogin.do"

headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
post_data = {"email":"mr_mao_hacker@163.com","password":"alarmchime"}

session.post(post_url,headers=headers,data=post_data,timeout=3)


url = "http://www.renren.com/327550029/profile"

response = session.get(url)

with open("renren3.htmal","w", encoding="utf-8") as f:
    f.write(response.content.decode())
