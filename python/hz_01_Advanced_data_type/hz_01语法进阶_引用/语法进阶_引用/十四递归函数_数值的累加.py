# 1 .定义个函数 sum_number()
# 2 .接收参数为 sum
# 3. 计算 1+2+3+4。。。。。sum 的结束
def sum_number(sum):

    # 1 .出口
    if sum == 1:
        return 1
    # 数字的累加 sum+ (1..sum -1)
    # 正确处理累加
    tem = sum_number(sum-1)

    # 两个数的累加
    return sum+tem

gl_sum = sum_number(6)
print(gl_sum)