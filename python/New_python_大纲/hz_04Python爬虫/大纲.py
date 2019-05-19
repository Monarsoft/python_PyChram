# 爬虫概念、工具和HTTP
###  1.什么是爬虫
—	爬虫就是：模拟客户端（浏览器）发送网络请求’，获取响应，按照规则提取数据的程序

—	‘模拟客户端（浏览器）发送网络请求’：照着浏览器发送一模异样的请求，获取和浏览一模一样的数据

## 2 。爬虫的数据去哪儿了
—呈现出来：展示在网页上，或者是展示在APP上
—进行分析：从数据中寻找一些规律

## 3. 需要的原件和环境
—Python3
	—黑马Python基础班15天视频
	：httP://yun.itheima.ocm/course/214.html
	—基础语法 （字符串，列表，字典，判断循环）
	—函数（函数的创建和调用）
	—面向对象（如何创建一个类，如何使用这个类）

—pycharm
	—Python编程

—Chrome浏览器
	—分析网络请求用的

## 4. 浏览器的请求
—url
	—在Chrome点击右键选择检查，点到network,
	—url = 请求的协议 + 网站的域名 + 资源的路径 + 参数

—浏览器请求url 地址
	—当前url对应的响应 + js + css + 图片 - - -》 elements中的内容
—爬虫请求url地址
	—当前url对应的响应
—elements的内容和爬虫获取到的url地址的响应不同，爬虫中需要以当前url地址对应的
响应为准提取数据

—当前url地址对应的响应在哪里
	—从network中找到当前的url地址，点击response
	—在页面上右键显示网页源码



## 5. 认识HTTP、HTTPS
	-- HTTP:超文本传输协议
		--以明文的形式传输
		--效率高，但是不安全
	--HTTPS:HTTP + SSL（安全套接字层）
		--传输之前数据先加密，之后解密获取内容
		--效率低，但是安全

—get请求和post请求区别
	—get请求没请求体，post有，get请求把数据放到url地址中
	—post请求常用于登录注册，
—post请求携带的数据量比get请求大，多，常用于传输大文本的时候

—HTTP协议之请求
	—1.请求行
	—2.请求头
	—3.User-Agent：用户代理：对方服务器能够通过user_agent知道当前请求对方资源的是什么浏览器
	—如果我们需要手机版的浏览器发送请求，对应的，就需要
	把user_agent改成手机版
	—Cookie：用来存储用户信息的，没吃请求会被携带上发送给对法的浏览器
		—要获取登录后才能访问的页面
		—对方的服务器会通过Cookie来判断我们是一个爬虫
—3. 请求体
	—携带体
	—get请求没有请求体
	—post请求有请求
—HTTP协议之响应
	—响应头
		—Set-Cookie： 对方服务器通过该字段设置cookie到本地
	—响应体
		—url地址对应的响应
 
## request模块学习

## 使用事前
	—pip install reqeusts
	

### 发送get ， post请求，获取响应
—response = requests.get(url)  # 发送get请求，请求url地址对应的响应
—response = requests.pos（url ，data = {请求体的字典}） ## 发送post请求

### response 的方法
—response . text
	—该方式往往会出现乱码，出现乱码使用response .encoding=“utf-8”
—response.content.decode()
	—把响应的二进制字节流转化为str类型

—response.requests.url 	# 发送请求的url地址
—response.url 	#response 响应的url地址
—response.requests.headers 	#请求头
—response.headers 	#响应请求

###  获取网页源码的正确打开方式（通过下面三种方式一定能够获取到网页的正确解码之后的字符串）
—	1.、response.content.decode()
—	2 、response.content.decode(“gbk”)
—	3 、response.text


### 发送带header的请求
—为了模拟浏览器，获取和浏览器一模一样的内容
、、、Python
Headers = {"User-Agent”: “
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36“}

response = requests.get（url ，headers=headers）

## 使用超时参数
—response.get(rul ,headers=headers,timeout=3)  # 3秒必须返回响应，否则会报错 


## retrying模块的学习
— pip install retrying 
\\\Python
from retrying import retry 

@retry(stop_max_attempt_number=3)
def fun1():
	print ("this is func1")
	raise ValueError("this is test error")
	
\\\


### 处理cookie相关的请求
—人人网{"email":"mro_mao_hacker@163.com",
"password":"alarmchime"}
—直接携带cookie请求url地址
	— 1、cookie放在headers中
	"""Python
	headers={"User-Agent”:"....","cookie":"cookie 字符串"}
	"""
	—2、cookie字典传给cookie参数
		—requests.get(rul,cookie=cookie)
		
	—、发送post请求，获取cookie，带上cookie请求登录的页面
		—1.session = request.session() # session具有的方法和requests一样
		—2.session.post(rul ,data ,headers=headers) # 服务器设置在本地的cookie，把cookie保存在session中	
		—3.session.get(url) # 会带上之前保存session中的cookie，能够请求成功
		
		
		
		
""" 第三部分"""

## 数据提取方法

### json
- 数据交换格式，看起来想用Python类型（列表，字典）的字符串
- 使用json之前需要的导入

- 哪里会返回json的数据
	- 浏览器切换到手机版
	- 抓包app
	
- json。loads
	- 把json字符串转化为Python 类型
	- json.loads(json字符串)
		
	
- json.dumps
	- 把python类型转化为json字符串
	- json.dumps({})
	- json.dumps(ret1,ensure_ascii=False,index=2)
		- ensure_ascii :让编码显示成中文
		- indent :能够让下一行在上一项的基础上空格
- 豆瓣电视爬虫案例




### xpathlxml
- xpath
	- 一门从html中提取数据的语言
- xpath 语法
	- xpath helper插件：帮助我们从'elements中定位数据
	- 1.选择节点（标签）
		- "/html/head/meta":能够选中html下的head下的所有
			的meta标签
	- 2."//":能够从任一节点开始选择
		- "//li": 当前页面上的所有li标签
		- "/html/head//link"： head下的所有link标签
	- 3. "@符号用途"
		-选择具体某个元素:"//dive[@class = "feed"]/ul/li
			- 选择class="feed"的dive下的li
			- "a/@href" :选择a的href的值
			
	- 4. 获取文本：
		- "/a/text()" :获取a下的文本
		- "/a//ext()" :获取a下的所有文本
	- 5.当前
		- “./a” 当前节点下的a标签 
	

- lxml
	- 安装：pip install lxml
	- 使用
	、、、python
	from lxml import etree
	element = etree.HTML("html字符串")
	element.xpath("")
	、、、
	
### 基础知识点的学习
- format:字符串格式化的一种方式
	``` python 
	"传智{}博客".format(1)
	"传智{}播客".format([1,2,3])
	"传智{}播客".format({1,2,3})
	"传智{}播客{}".format({1,2,3},[1,23,2])
	"传智{}播客{}".format({1,2,3},1)
	
- 列表推导式
	- 帮助我们快速的生成包含一堆数据的列表
	`[i+10 for i in range(10)]`--->[10,11,12,...,19]
	`["10月{}日".format(i) for i in range(1,20)]`
	--->["10月1日","10月2日","...","10月9日"]
	
- 字典推导式
	- 帮助我们快速的生成包含一堆数据的字典
	``` python
	{: for in range(10)}
	#{10:0,11:1,12:3,...,19:9}
	```





	