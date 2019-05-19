# encoding = "utf-8"
import json
import requests
from parse import parse_url

class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1534255320421"
    
    def get_contentf_list(self,html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list,total

    def save_content_list(slef,content_list):
        with open("douban.json","a", encoding = "utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")


    def run(self): # 实现主要逻辑
        sum = 0
        total = 120
        while sum < total:
            # 捕获事件
            #evet_get = pygame.event.get()
            #1 start_url
            star_url = self.temp_url.format(sum)
            #2 发送请求获取数据
            html_str = parse_url(star_url)
            # print(html_str)
            #3 提取数据
            content_list = self.get_contentf_list(html_str)
            #4 保存
            self.save_content_list(content_list)
            #5 构造下一页URL地址
            sum +=18
            print("保存成功：%d" %sum)


if __name__=="__main__":
    douban = DoubanSpider()
    douban.run()
