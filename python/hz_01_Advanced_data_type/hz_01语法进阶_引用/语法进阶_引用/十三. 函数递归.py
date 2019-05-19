def demo_numbers(sum):

    print("sum:%d" %sum)

    if sum == 1:
        return sum
    # 递归自己调用自己
    demo_numbers(sum-1)

demo_numbers(3)