#include"stdio.h"
main()
{
	float s=0;
	for(float i=1;i<100;i+=2)
		s+=1.0/i;
	printf("1+1/3+1/5+1/7+...+1/99=%f",s);
}
