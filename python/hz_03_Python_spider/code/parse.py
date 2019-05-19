import requests
from retrying import *
import json
from lxml import etree

#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
#query_sting = {"query":"百度"}

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36","Referer": "no-referrer-when-downgrade"}

@retry(stop_max_attempt_number=3) # 让封装的函数最多执行三次，如果三次都错误，就返回错误。其中
                                  # 执行没有出现错误则继续往下执行
def _parse_url(url):
    print("_ _ "*10)
    response = requests.get(url,headers=headers, timeout = 3) # timout函数：最多给三秒响应时间
    return response.content.decode()
def pase_parse_url(content_str):
    html_str = _parse_url(content_str)
    div_html = etree.HTML(html_str)
    item = {}
    item["name"] = div_html.xpath("//div")


    return item


if __name__ == "__main__":
    ret = pase_parse_url("http://yun.itheima.com/")
    # print(ret[:100000])  # 取前100个http://yun.itheima.com/
    print(ret)