import requests,json
from lxml import etree

url = "https://movie.douban.com/chart"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

response = requests.get(url,headers=headers)
html_str = response.content.decode()

#1 使用etree处理数据
html = etree.HTML(html_str)

#1. 获取所有电影url地址
html_list = html.xpath("//div[@id='wrapper']//div[@class='indent']//a/@href")
#print(html_list)
#2. 获取所有图片地址
img_html = html.xpath("//div[@id='wrapper']//div[@class='indent']//a/img/@src")
#print(img_html)

#3. 吧每部电影组成字典，字典中是电影的各种数据，比如：标题、utl、图片地址、评论数、评分
# 思路：
    #1.分组
    #2.每一组提取数据
ret1 = html.xpath("//div[@id='wrapper']//div[@class='indent']/div/table")
item = {}
for table in ret1:
    item["title"] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    item["href"] = table.xpath(".//div[@class='pl2']/a/@href")
    item["img"] = table.xpath(".//a[@class='nbg']/img/@src")
    item["rating_nums"] = table.xpath(".//div[@class='pl2']/div//span[@class='rating_nums']/text()")[0]
    item["comment_nums"] = table.xpath(".//div[@class='pl2']/div//span[@class='pl']/text()")[0]
    print(item)