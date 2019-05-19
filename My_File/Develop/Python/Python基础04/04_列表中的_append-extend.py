#coding=utf8
'''
append 和extend 的区别
'''

#infors = {"name":"桃子","phone":"1000000","email":"1000000@inf.com"}
names = ["小顺子","小德子","小李子"]
names2 = ["桃子","胖墩"]
names3 = ["刘玲","宗介"]

# append
names2.append(names)
print(names2)

# extend
names3.extend(names)
print(names3)

