# _*_ coding: utf-8 _*
class Person(object):
    '''人类'''
    def __init__(self, name):
        self.name = name #用来记录人的姓名
        self.naqide_qiang = None # 把枪拿在手上

    def anzhuang_zidian(self, clip_temp, bullet_temp):
        '''把子弹装进弹夹'''

        # 弹夹保存子弹
        clip_temp.baocun_zidan(bullet_temp)

    def anzhuang_danjia(self, AK47_temp, bullet_AK47):
        '''把弹夹安装到枪中去'''
        self.bullet_AK47 = bullet_AK47 # 用于拿枪时知道子弹的信息
        # 枪保存弹夹
        AK47_temp.zhuzhuang_danjia(bullet_AK47)
    def laowang_naqide_qiang(self, AK47_temp):
        '''老王拿起枪'''

        self.naqide_qiang = AK47_temp # 拿枪
    def __str__(self):
        if self.naqide_qiang != None:
            return "%s信息:%s拿起%s 子弹：%d/%d"%(self.name, self.name, self.naqide_qiang.name, len(self.bullet_AK47.zidian_list), self.bullet_AK47.maxnum)
        else: print("%s没有枪！", self.name)

class Gun(object):
    '''枪类'''
    def __init__(self, name):
        self.name = name #用于记录枪的型号
        self.danjia = None # 用来记录弹夹对象引用

    def zhuzhuang_danjia(self, bullet_AK47):
        '''安装弹夹'''

        self.danjia = bullet_AK47

    def __str__(self):
        if self.danjia != None:
            return "枪的信息：%s"%(self.name)
        else: print("没有弹夹！")

class DanJa(object):
    '''弹夹类'''
    def __init__(self, maxnum):
        self.maxnum = maxnum # 记录弹夹的最大容量
        self.zidian_list = [] #用于记录所有子弹的引用

    def baocun_zidan(self, bullet_temp):
        '''保存这颗子弹'''
        self.zidian_list.append(bullet_temp)

    def __str__(self):
        return "弹夹的信息：%d/%d"%(len(self.zidian_list), self.maxnum)

class ZiDan(object):
    '''子弹类'''
    def __init__(self, kilmax):
        self.kilmax = kilmax

def main():
    '''用来控制整个流程'''
    
    #1.创建一个老王
    laoWang = Person("老王")

    #2.创建一个抢
    AK47 = Gun("AK47")

    #3.创建一个弹夹
    clip = DanJa(100)
    for i in range(15):
        #4.创建一些子弹
        bullet = ZiDan(100)

        #5.老王把子弹装进弹夹
        laoWang.anzhuang_zidian(clip, bullet)

    #6.把弹夹装在枪上
    laoWang.anzhuang_danjia(AK47, clip)

    #Tests：测试弹夹信息
    print(clip)

    #Test：测试枪的信息
    print(AK47)

    #7.老王拿起枪
    laoWang.laowang_naqide_qiang(AK47)
    print(laoWang)

    #8.创建一个敌人

    #9.老王开抢打敌人


if __name__ == "__main__":
    main()

