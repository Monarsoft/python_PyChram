def demo(*arg,**kward):

    print(arg)
    print(kward)



gl_arg = (1,2,3,4,5)
gl_kard = {"naem":"小明","age":19}

#demo(gl_arg,gl_kard)
# 使用拆包语法 ，可以简化元组、字典变量的传递
# 拆包只需要 在变量前面加*，元组加一个*、字典两个*
#demo(*gl_arg,**gl_kard)

demo(1,2,3,4,5,name="小明",age=19)