# 火车安检嵌套
matter = input("票：有/没有：\n")
if(matter == "有"):
    matter2 = input("请过安检，是否有危险物品：有/没有\n")
    if matter2 == "有":
        print("危险物品不能带入")
    else:
        print("请进")
else:
    print("必须出示票证")