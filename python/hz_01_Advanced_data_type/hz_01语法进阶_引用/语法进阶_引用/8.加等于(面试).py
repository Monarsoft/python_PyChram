def demo(sum,sum_list):
    print("函数开始")
    # sum = sum+sum 
    sum += sum
    
    # 列表 变量使用 + 不会做相加在赋值的操作
    #sum_lsit = sum_list + sum_list
    # 本质上是在调用exdent方法, exdent方法不会修改引用，不会修改引用就会影响外部数据
    sum_list += sum_list
    #sum_list.extend(sum_list)

    print(sum)
    print(sum_list)
    print("函数结束")


gl_sum = 9
gl_list = [1,2,3]
demo(gl_sum,gl_list)
print(gl_sum,gl_list)