# cat color.py 

#!/usr/bin/env python
# -*- coding: utf-8 -*-
while 1:
    # 字体颜色
    print ("=====字体颜色======")
    for i in range(31, 38):
        print ("\033[%s;40mHello world!\033[0m" %i)
    # 背景颜色
    print ("=====背景颜色======")
    for i in range(41, 48):
        print ("\033[47;%smHello world!\033[0m" %i)
    # 显示方式
    print ("=====显示方式======")
    for i in range(1, 9):
        print ("\033[%s;31;40mHello world!\033[0m" %i)
