# 导入某个模块类/函数或变量等 , 只需要直接使用，不需要模块名点的方法
# 开发中不推荐使用from import 导入 同名函数会被最下方的覆盖
from hz_01_测试模块1 import say_hello
from hz_02_测试模块2 import say_hello

say_hello()
