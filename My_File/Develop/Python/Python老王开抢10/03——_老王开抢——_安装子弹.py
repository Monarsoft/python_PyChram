# _*_ coding: utf-8 _*
class Person(object):
    '''人类'''
    def __init__(self, name):
        self.name = name #用来记录人的姓名

    def anzhuang_zidian(self, clip_temp, bullet_temp):
        '''把子弹装进弹夹'''

        # 弹夹保存子弹
        clip_temp.baocun_zidan(bullet_temp)


class Gun(object):
    '''枪类'''
    def __init__(self, name):
        self.name = name #用于记录枪的型号

class DanJa(object):
    '''弹夹类'''
    def __init__(self, maxnum):
        self.maxnum = maxnum # 记录弹夹的最大容量
        self.zidian_list = [] #用于记录所有子弹的引用

    def baocun_zidan(self, bullet_temp):
        '''保存这颗子弹'''
        self.zidian_list.append(bullet_temp)

class ZiDan(object):
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
    laoWang.anzhuang_zidian(clip, bullet)

    #6.把弹夹装在枪上
    #laoWang.anzhuang_danjia(AK7, clip)

    #7.老王拿起枪

    #8.创建一个敌人

    #9.老王开抢打敌人


if __name__ == "__main__":
    main()

