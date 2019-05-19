# 、导入包
import pygame
pygame.init()
mell = ("aaa","aaa","aaa",99)  # 元组
mell = ["444","4aa",99]   #列表
mell = {"a","a","a"}
mell = ({"adfasdf"},{"adfasdf",99})
mell = ("aa")
print(type(mell))

def mal():
    e = float(input("输入苹果的单价、"))
    e *= float(input("输入苹果的 重量"))
    
    print("总价：%0.2f"  %e)

def famney():

    print(True, False * 2)
    print("he"+"llo")
    scal = 2.5
    print("%0.0f%%" % (scal*10))
    if True is scal: # 是否是内存中在同一片地址
        print("True")
    else:
        print("else")
        pass

def logic():
    age = 120

    if age >=0 or age <=120:
        print("成立")
    if age >=0 and age <=0:
        print("pass")
    if not  age:
        print("not True")
      
def QianTao():
    man = input("是否有票：")
    if man == "有" or man == "yes":
        print("请到检查站检查、！")
        knife = float(input("knife的长度是："))
        if knife <13:
            print("请上车")
        else:
            print("Knife 超过安全长度，不能进入")
    else:
        print("请到柜台购票，")
    pass

def ChengFa(): 
    len = 1
    while len<=9:
        i=1
        while i<=len:
            print("%d*%d=%d\t" %(i,len,len*i), end="")
            i +=1
        print()
        len +=1

    col = 1

    pass


def clas():
    tuple = ("小娟",20,19,20)
    print(tuple.index("小娟"))
    print(tuple.count("小娟"))
    #增

    #删

    #该

    list = ["p","y","t","h","o","n"]
    #增
    list[5] = "n pygame"
    list.append("pygame")    
    #list.index(1)
    list.insert(1,"haha")
    extend = ["Extend"]
    list.extend(extend)
    #删
    list.remove("pygame")
    list.pop(1) 
    #list.clear()
    #该
    dictionary = {"name":"小米","age":8}
    for i in dictionary:
        print(dictionary[i],end ="")
    #增

    #删

    #该
    charcter = "hello world"
    print(charcter.count("hello world"))
    #增
    
    #删

    #该

    print(type(tuple))
    print(tuple)
    print(type(list))
    print(list)
    print(type(dictionary))
    print(dictionary)
    print(type(charcter))
    

clas()








pygame.quit()
