#include <stdio.h>

int main(void) {
	
	int y, len;

	scanf("%d", &y);
	len = sizeof(y)/sizeof(y);

	printf("%d", y);
	/*
	int i,len=0;
	printf(" 1~100 能被3和2整出的有：");
	for (i=1; i<=100; i++){
		if (i%2==0 && i%3==0){
			printf("%d ", i);	
			len++;
		}

	}
	printf("\n符合要求的个数为:%d\n", len);


	/*
	int intger = 100, i, len=0;
	for (i=0; i<100; i++) {
		if ((intger%3 == 0 )&&( intger%2 == 0)){
			len+=1;
			//printf("-----------------------------------");
		}
		intger --;
	
	}
	printf("sum:%d\n", len);

	/*
	int m=19,n=5,p;
	char y=17.3;
	int ch = m/n+(p=(y/2+0.5));
	printf("%d", ch);

	/*
	int s1,s2;
	scanf("%d %d", &s1, &s2);
	printf("\n%d:%d\n", s1, s2);
	s1 = s1-s2;
	s2 = s1+s2;
	s1 = s2-s1;
	printf("-------------------------------------------\n");
	printf("%d:%d\n", s1, s2);
	
	/*
	char ch;
	int a=6,b=4,c=2;
	int e=NULL;
	e = !(a-b)+c-1 && b+c/2;
	printf("%d", e);
	ch = getch();
	putchar(ch+10);
	/*
	int x,y;
	int d=241;

	//scanf("%d %d", &x,&y);
	x = d/100%9;
	y = (-1)&&(-1);

	printf("x = %d;Y = %d\n", x,d);
*/
	return 0;

}
