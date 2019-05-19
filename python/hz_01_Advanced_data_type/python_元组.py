list_naem =("pop","reverse","remove")
print("%s"%list_naem[0])
print(list_naem.index("pop"))
for nae in list_naem:
    print("nae:",nae)

list_fon = ("小米",19,1.87)
print("%s的年龄是 %d  身高是 %f",list_fon)     #格式化语句

list_fonin = "%s的年龄是 %d  身高是 %f",list_fon
print(list_fonin)
print(type(list(list_fonin)))  #list()函数 把元组类型转换成列表类型
print(type(tuple(list_fonin)))  #tuple()函数 再把列表类型转换成元组类型