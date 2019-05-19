#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int a[100]/*用于保存10个产生的随机数*/, i;
    srand((unsigned int)time(NULL));//设置当前时间为种子
    for (i = 0; i < 10; ++i){
        a[i] = rand()%10+1;//产生1~10的随机数
    }
    //打印生成的随机数
    for (i = 0; i < 10; ++i){
        printf ("%d ", a[i]);
    }
    printf ("\n");
    return 0;
}