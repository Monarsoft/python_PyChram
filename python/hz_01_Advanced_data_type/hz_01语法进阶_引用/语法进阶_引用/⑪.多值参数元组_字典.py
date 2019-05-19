def demo(sum,*args,**kword):
    print(sum)
    #便利
    for f_args in args:
        sum = f_args+sum # 元组中数值的累加
        print(f_args)
    print(args)

    for f_kword in kword:
        print(kword[f_kword])
    print(kword)

    return sum


gl_sum = demo(1,1,2,3,4,5,6,name="小美",age=19)
print("sum:%d" %gl_sum)