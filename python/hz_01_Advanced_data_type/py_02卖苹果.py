#卖苹果的单价
privat = int(input("单价：")) #同时把str类型转换整型
#苹果的重量
lengt = float(input("重量："))
#需要付费的金额
zongjia = privat*lengt
print("单价%d元/kg; 重量 %0.2f kg  " %(privat,lengt))
print("应付金额 %0.2f 元"% zongjia )