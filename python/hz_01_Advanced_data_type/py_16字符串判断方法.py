# 1.判断空白字符
space_str = "   \n\r\t\v"
print(space_str)
print(space_str.isspace())
# 2. 判断字符串中是否包含数字
# star_str = "3"
# space_str = "3\u00b2"
space_str = "贰"
print(space_str)
print(space_str.isdecimal())    # isdecimal() 方法只能判断纯数字
print(space_str.isdigit())      # isdigit()   方法可以判断特殊字符
print(space_str.isnumeric())    # isumeric()  方法可以判断中文数字