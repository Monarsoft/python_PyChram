/*2、	用C编写一段程序，实现任意输入3个数值后输出其中的最大值。
要求：由main()函数实现数值的输入输出，
最大值由float max(float x,float y,float z)求解。
*/

#include <stdio.h>

float max(float x,float y, float z);
int main(void){
	float x,y,z;
	scanf("%f", &x);
	scanf("%f", &y);
	scanf("%f", &z);
	int mx = max(x,y,z);
	printf("Max:%0.2f", mx);
	
	return 0;
}
float max(float x, float y, float z){
	float mx = 0;
	mx = (x>y?x:y)>z?(x>y?x:y):z;
	return mx;
	
	
}