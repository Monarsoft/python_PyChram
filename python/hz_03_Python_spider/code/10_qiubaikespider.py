import requests
from lxml import etree
import json
class QiubaiSp():
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

    def get_url_list(self): # 根据url地址的规律，构造url list
        self.url_lsit = [self.url_temp.format(i) for i in range(1, 15)]
        return  self.url_lsit

    def pase_url(self,url): # 发送请求
        response = requests.get(url, headers=self.headers)
        return  response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        dive_lsit = html.xpath("//div[@id='content-left']/div")
        for div in dive_lsit:
            item = {}
            item["author_name"] = div.xpath(".//h2/text()")[0] if len(div.xpath(".//h2/text()"))>0 else None
            item["span"] = div.xpath(".//a/div/span/text()")
            item["number"] = div.xpath(".//div/span/i/text()")
            item["评论"] = div.xpath(".//div/a/i")
        # print(type(item))
        return item

    def save_content_list(self, content_list):
        with open("QSBKS.TXT", "w", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功!")

    def run(self): # :实现主要逻辑
        # 1. 更具url地址的规律，构造url list
        url_list =self.get_url_list()
        # 2. 发送请求获取响应
        for url in  url_list:
            html_str = self.pase_url(url)
            # 3. 提取数据
            html_result = self.get_content_list(html_str)
            # 4. 保存
            self.save_content_list(html_result)
            print(html_result)
            # print(url)
        pass

if __name__ == "__main__":
    qiubaispider = QiubaiSp()
    try:
        qiubaispider.run()
    except Exception as result:
        print(result)
