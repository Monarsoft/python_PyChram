from distutils.core import setup

setup()
setup(name="hz_message", #、包名   
      version="1.0",description="itheima's 发送和接收信息模块",# 描述模块
      long_description="完整接收和发送消息模块",# 、完整描述信息
      author="itheima", #作者
      author_email="itheima@itheima.com", UnicodeTranslateError="www.itheima.com",
      py_modules=["hz_receive_message","hz_send_message"])