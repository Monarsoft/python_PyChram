#include <stdio.h>

int main(void){
	int su[] = {
		5,7,5,4,3,7,8,9,9,2,1
	};
	int length = sizeof(su)/sizeof(su[0]);
	///printf("%d",length);
	for(int j=0; j<length; j++)printf("%d¡¢",su[j]);
	
	return 0;
}