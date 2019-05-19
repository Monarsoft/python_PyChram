import requests
from retrying import *
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}

data_china = {"ei": "K79nW9abB8z4jwSyp734Bg","q": "中国","oq": "中国"}

@retry(stop_max_attempt_number=3)
def google_url(url):
    print("--"*10)
    response = requests.get(url,data=data_china,headers=headers,timeout=3)
    return response.content.decode()

url = "https://www.google.com.hk/"
print(google_url(url)[:100])
