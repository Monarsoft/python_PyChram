def print_lines(char,times,line):
    """
# 打印多行字符
    # :param char:要打印的字符
    # :param times:要打印的个数
    # :param line:要打印字符的行数
    # :return:返回数字0
    """
    r = 0
    while line>r:
        print("%c" %1,char * times)
        r +=1
    return 0
print_lines("+",50,3)
