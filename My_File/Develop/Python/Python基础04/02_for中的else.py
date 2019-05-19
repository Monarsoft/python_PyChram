#coding=utf8
'''
while 、for 遍历列表
'''
nums = [11,22,33,44,55,66]

'''
i = 0
while i < len(nums):
    print(nums[i])
    i +=1
'''
new = int(input("查找："))
for temp in nums:
    if new == temp:
        print("找到了！")
        break
else:
    print("没有找到！")

