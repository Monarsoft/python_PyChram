# _*_ coding: utf-8 _*_
print("Hell 你好！")
class Person(object):
    '''人类'''
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name #用来记录人的姓名
        self.bullet = None # 弹夹
        self.naqide_qiang = None # 把枪拿在手上
        self.hp = 100

    def anzhuang_zidian(self, clip_temp, bullet_temp):
        '''把子弹装进弹夹'''

        # 弹夹保存子弹
        clip_temp.baocun_zidan(bullet_temp)

    def anzhuang_danjia(self, AK47_temp, bullet_AK47):
        '''把弹夹安装到枪中去'''
        self.bullet = bullet_AK47 # 用于拿枪时知道子弹的信息
        # 枪保存弹夹
        AK47_temp.zhuzhuang_danjia(bullet_AK47)
    def laowang_naqide_qiang(self, Gum_temp):
        '''老王拿起枪'''


        self.naqide_qiang = Gum_temp # 拿枪

    def kou_banji(self, enemy_temp):
        '''老王开抢让子弹打敌人'''
        # 弹出一颗子弹伤害敌人
        self.naqide_qiang.fire(enemy_temp)

        # 让子弹伤害敌人
    def diao_xue(self, sha_sahang_li):
        '''根据子弹的威力掉相应的血'''
        self.hp -= sha_sahang_li

    def __str__(self):
        if self.hp:
            if self.naqide_qiang != None:
                #return "%s信息:%s拿起%s 子弹：%d/%d"%(self.name, self.name, self.naqide_qiang.name, len(self.bullet_AK47.zidian_list), self.bullet_AK47.maxnum)
                return "%s的血为:%d%% TA有枪!  %s %s"%(self.name, self.hp, self.naqide_qiang, self.bullet)
            else: 
                return "%s的血为:%d%% TA没有枪！%s %s"%(self.name, self.hp, self.naqide_qiang, self.bullet)
        else:
            return "敌人挂了。。。。"

class Gun(object):
    '''枪类'''
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name #用于记录枪的型号
        self.danjia = None # 用来记录弹夹对象引用

    def zhuzhuang_danjia(self, bullet_AK47):
        '''安装弹夹'''

        self.danjia = bullet_AK47

    def fire(self, enemy_temp):
        '''获取一发子弹，让子弹击中敌人'''

        # 从弹夹中取子弹
        zidan_temp = self.danjia.tanchu_zidan()

        # 让子弹伤害敌人
        if zidan_temp:
            zidan_temp.da_zhong(enemy_temp)
        else:
            print("没有子弹了。。。。。。")

    def __str__(self):
        if self.danjia:
            return "枪的信息：%s"%(self.name)
        else: 
            return "没有子弹！"

class DanJa(object):
    '''弹夹类'''
    def __init__(self, maxnum):
        self.maxnum = maxnum # 记录弹夹的最大容量
        self.zidian_list = [] #用于记录所有子弹的引用

    def baocun_zidan(self, bullet_temp):
        '''保存这颗子弹'''
        self.zidian_list.append(bullet_temp)

    def __str__(self):
        return "弹夹的信息:%d/%d"%(len(self.zidian_list), self.maxnum)

    def tanchu_zidan(self):
        '''弹出一颗子弹'''
        if self.zidian_list:
            return self.zidian_list.pop()
        else:
            return None


class ZiDan(object):
    '''子弹类'''
    def __init__(self, kilmax):
        super(ZiDan, self).__init__()
        self.sha_sahang_li = kilmax

    def da_zhong(self, enemy_temp):
        '''让敌人掉血'''
        enemy_temp.diao_xue(self.sha_sahang_li)

def main():
    '''用来控制整个流程'''
    
    #1.创建一个老王
    laoWang = Person("老王")

    #2.创建一个抢
    AK47 = Gun("AK47")

    #3.创建一个弹夹
    clip = DanJa(10)
    for i in range(15):
        #4.创建一些子弹
        bullet = ZiDan(10)

        #5.老王把子弹装进弹夹
        laoWang.anzhuang_zidian(clip, bullet)

    #6.把弹夹装在枪上
    laoWang.anzhuang_danjia(AK47, clip)

    #Tests：测试弹夹信息
    #print(clip)

    #Test：测试枪的信息
    #print(AK47)

    #7.老王拿起枪
    laoWang.laowang_naqide_qiang(AK47)

    #Test:测试老王的信息
    print(laoWang)

    #8.创建一个敌人
    laoSu = Person("西路")

    for i in range(10):
        #9.老王开抢打敌人
        laoWang.kou_banji(laoSu)

    #Test:测试敌人
    print(laoSu)

    #Test:测试老王开抢打敌人
    print(laoWang)

if __name__ == "__main__":
    main()

