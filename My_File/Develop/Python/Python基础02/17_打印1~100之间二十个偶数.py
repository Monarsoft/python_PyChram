#codin=utf8
'''
程序实现打印1~100之间的偶数
'''
integer = 101
'''
for i in range(1,integer):
    if i%2 == 0:
        print("%d "% (i), end="")
'''
'''
while integer > 0:
    if integer%2 == 0:
        print("%d "% (integer),end="")
    integer -=1
    '''
integer = 2
sun = 1
print("="*80)
while integer <= 100:
    if integer%2 == 0:
        print("%d "%(integer),end="")
        if sun == 20:
            break
        sun +=1
    integer += 1
print("(总计 %d 个偶数)"%(sun),end="")
print("")
print("="*80)
