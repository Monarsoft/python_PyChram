import requests
from lxml import etree
import json

class BlogDer(object):
    def __init__(self):
        self.url_temp = "https://www.cnblogs.com/#p{}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                        "referer": "https://www.cnblogs.com/",
                        "cookie": "_ga=GA1.2.110321801.1533730130; _gid=GA1.2.1588916287.1536243757; __gads=ID=405664a68e313211:T=1536295319:S=ALNI_MZsaDfyLj5eKdC1-J1sjUKlB_-Fxw; .CNBlogsCookie=FE9054FFDB70A552DB5E74CEBE55EE0208C2BCAD81C49DF5B5843BF8A2F537AB265517F2D6292DBE58E208D9ACA282BA4468BCDA3A538362BE5F0B8496526C6B0EA154C4712D77F60884B203D004448AD3E8C64E; .Cnblogs.AspNetCore.Cookies=CfDJ8J0rgDI0eRtJkfTEZKR_e80sWLJPc8r46QmkPw7j1n7YhAoTIRXKEnhsOnFTKbMQKiVas4Rbux2mI4RiZJdUK5TGtWM2IZJ7ADdq_d8KqqLQbIJqyaLYqoGTqVRHPZS2RzwpXhGE7dPhFpZRpUmSHCTh1aMu4vzWvDu1YXUpGtmqY6uwhMJMe7Ck8fq7aAN9tQZxloBWhHrds4XRMeLrLc-BNAG7M2aJN5DtwpVNGIJfdC47OWMNGGhZeD5nPYsQdTf_WQfE3QvH37luXLxVkBuDVPo0Hdd78KQW89rgYeRa; _gat=1"}

    def get_ulr_list(self): # 构造url地址
        self.url_list = [self.url_temp.format(i) for i in range(1, 13)]
        return self.url_list

    def pase_url(self, url_list): # 获取响应
        response = requests.get(url_list, headers=self.headers)
        return response.content.decode()

    def get_content_list (self, html_str):
        html = etree.HTML(html_str)
        print(html)
        div_html = html.xpath("//div[@id='post_list']/div")
        item = {}
        for div in div_html:
            item["target_name"] = div.xpath(".//h3/a/text()")[0] if len(div.xpath(".//h3/a/text()"))>0 else None
            item["img"] = div.xpath(".//p/a/img/@src")
            item["content"] = div.xpath(".//p/text()")

        return item

    def save_content_list(self, html_result):
        with open("博客.txt", "a", encoding="utf-8") as f:
            for content in html_result:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功!")

    def run__(self):
        # 1.构造url地址
        self.url_list = self.get_ulr_list()
        # 2.发送请求获取响应
        for url in self.url_list:
            self.html_str = self.pase_url(url)
            # 3.提取数据
            self.html_result = self.get_content_list(self.html_str)
            # print(self.html_result)
            # 保存内容
            self.save_content_list(self.html_result)
            print()
            print()

if __name__ == "__main__":
    blokeyuan = BlogDer()
    blokeyuan.run__()