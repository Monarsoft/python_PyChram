#include <stdio.h>
#define LENG 10

void maopao(int *);
void xuanzepaixu(int *);
int main(void){

    int array[] = {9,1,8,2,7,3,6,4,5,0};
    int len = 0;
    int i=0;

    printf("����ǰ");
    for (i=0; i<LENG; i++){
        printf("\a%d`",array[i]);
        }

    //ѡ��
   //xuanzepaixu(array);
    //ð��
    maopao(array);

    printf("\n");
    printf("�����");
    for (i=0; i<LENG; i++){
        printf("\a%d`",array[i]);
        }
    return 0;
}
 //select
 void xuanzepaixu(int *array){
    int i,j;

    for (i=0; i<LENG-1; i++){

        for(j=1; j<LENG-1-i; j++){
            if(array[i]>array[j]){
                array[i] = array[i]+array[j];
                array[j] = array[i]-array[j];
                array[i] = array[i]-array[j];
            }
        }
    }

 }

 //bubbling
 void maopao(int * array){

    int i,j;
    for (i=0; i<LENG-1; i++){
        for (j=0;j<LENG-1-i; j++){
            if (array[j]>array[j+1]){

                array[j] = array[j]^array[j+1];
                array[j+1] = array[j]^array[j+1];
                array[j] = array[j]^array[j+1];
            }
        }
    }
 }