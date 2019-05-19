#include <stdio.h>
#define LENG 10000

int stamp();
//int Seekt();
int AB(void);
int main(void){

    AB();

    return 0;
}


int AB(void){
    int PA,PB;
    int i,j,k;
    for(i=1000;i<LENG;i++){
        for(j=1; j<i-1; j++){
            if(i%j==0){
                PA +=j;
//                printf("%d\n",j);
            }

        }
        for (j=1; j<LENG;j++){
            if((LENG-1)%j==0){
                PB +=j;
            }
        }
        if(PB = PA)
            printf("%d->%d\n",j,j+1);

    }
}

















/*
//is seekt
int Seekt(void){
    int sz[] = {0,1,2,3,4,5,6,7,8,9};
    int L,R,i,j,p;
    L = 0;R = sizeof(sz)/sizeof(int);
    scanf("%d",&p);

    while(L<=R){
        int mid =(L+R)/2;
        if(sz[mid]==p)
            return mid;
        else if(sz[mid]<p)
            R = mid-1;
        else
            L = mid+1;

    }

    return mid;
}

*/


















//选择排序
int stamp(void){
    int sz[] = {1,9,3,7,4,6,5,8,2,0};
    int n = sizeof(sz)/sizeof(int);
    int r,i,j,temp;

    for(r=0;r<n; r++)
        printf("%d",sz[r]);
    printf("\n");

    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(sz[i]>sz[j])
            {
                temp=sz[i];
                sz[i]=sz[j];
                sz[j]=temp;
            }
        }
    }
    for(r=0;r<n; r++)
            printf("%d",sz[r]);

    return 0;
}
