#coding=utf8
'''
复习while中break
'''
i = 1
print("="*80)
while i<=9:
    if i == 3:
       #break
       continue
       #pass
    i +=1
    print("i = %d"% (i),end="")
    print("$")
print("="*80)

