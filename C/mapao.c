#include <stdio.h> 

void Sort(int * pArr, int len){
	
}
int main(void) {
	int a[6] = {10, 2, 8, -8, 11, 0};
	Sort(a, 6); 

	int i = 0;
	while(i<6){
		printf("%d ", a[i]);
		i++;
	}
	printf("\n");

	/*
	a = a^b;
	b = a^b;
	a = a^b;
	/*
	a = a+b;
	b = a-b;
	a = a-b;
	/*
		a = a-b;
	b = a+b;
	a = b-a;
	*/
//	printf("%d:%d", a,b);


	system("pause");
	return 0;

}