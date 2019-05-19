#、模块提供 函数、全局变量、类，注意：直接执行的代码不是向外界提供的工具

def say_hello():
    print("你好 我是 say hello")

#\ 直接执行的代码
if __name__ == "__main__":
    print(__name__)


    print("小明")
    say_hello()
