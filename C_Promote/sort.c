#include <stdio.h>
#define LEN = 3
void composite_number();
int main(void)
{
    // composite number
    composite_number();

    return 0;
}
//composite_number
void composite_number(){

    int i;
    int number = 0;
    printf("This  composite number?\n");
    scanf("%d",&number);
    if(number%2==0&&number%3==0)
        printf("%d Is composite number!\n",number);
    for(i=1; i<9; i++){
        if (number%i!=0)
            printf("%d Not's  composite number!\n",number);
    else printf("number");
    }
}