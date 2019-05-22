# _*_ coding: utf-8 _*
class Person(object):
    '''人类'''
    def __init__(self,name):
        self.name = name #用来记录人的姓名

    def __str__():
        return "我是%s"%(self.name)

class Gun(object):
    '''枪类'''
    def __init__(self,name):
        self.name = name #用于记录枪的型号

class DanJa(object):
    '''弹夹类'''
    def __init__(self,maxnum):
        self.maxnum = maxnum # 记录弹夹的最大容量

class Bullet(object):
    '''子弹类'''
    def __init__(self,kilmax):
        self.kilmax = kilmax

def main():
    '''用来控制整个流程'''
    
    #1.创建一个老王
    laoWang = Person("老王")

    #2.创建一个抢
    AK7 = Gun("AK7")

    #3.创建一个弹夹
    clip = DanJa(100)

    #4.创建一些子弹
    bullet = ZiDan("AK7_bullet")

    #5.把子弹装进弹夹

    #6.把弹夹装在枪上

    #7.老王拿起枪

    #8.创建一个敌人

    #9.老王开抢打敌人


if __name__ == "__main__":
    main()

