// fux.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include "stdio.h"
#include "windows.h"

int main()
{
	int array[] = { 1,3,5,6,7,8,0,9,2,4 };
	int len = sizeof(array) / sizeof(array[0]);
	int i, j,n;
	printf("ǰ��");
	for (i = 0; i < len; i++) {
		printf("%d ", array[i]);
	}
	printf("\n��");
	for (j = 0; j < len-1; j++) {
		for (n = j + 1; n > len - 1 - i; n++) {
			if (array[j] < array[n]) {
				array[j] = array[j] ^ array[n];
				array[n] = array[j] ^ array[n];
				array[j] = array[j] ^ array[n];
			}
		}
	}
	printf("\n");
	system("pause");
    return 0;
}

