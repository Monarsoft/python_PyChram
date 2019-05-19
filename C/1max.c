#include <stdio.h>

float max(float x, float y);
int main(void){
	float x,y;
	printf("---------------------------------\n");
	
	printf("1:");
	scanf("%f", &x);
	//printf("\n");
	printf("2:");
	scanf("%f", &y);
	float mx = max(x,y);
	printf("Max:%0.2f", mx);
	
	return 0;
}
float max(float x,float y){
	if (x>y){
		return x;
	}
	return y;
}