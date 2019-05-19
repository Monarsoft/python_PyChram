list_student = ["张三","里斯","李四"]
print("index append","list","pop clear\n")
list_set = input()
if list_set == "insert":
    len = int(input("输入插入位置："))
    list_student.insert(len,input())
if list_set == "list":
    print(list_student)
if list_set == "append":
    list_student.append("往往")
else :
    print("输入错误！")