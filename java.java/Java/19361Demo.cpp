# include <stdio.h>
int len = 0;
	int main(void) {
		
		
	int k=0;char c='A';
do
{
	switch(c++)
	{
		case 'A':k++;break;
		case 'B':k--;
		case 'C':k+=2;break;
		case 'D':k=k%2;continue;
		case 'E':k=k*10;break;
		default: k=k/3;
	}
	k++;
}
while(c<'G');
printf("k=%d",k);
		
		
		
		
		
			/*
			int i;
	for(i=1;i<=9;i++)
	{ 
	if(i%3)
		putchar(°Æ*°Ø);
	else continue;
		printf(°∞#°±);
	}
printf(°∞@°±);
		/*
		int a = 10, b = 0;
		do {
			b+=2;
			a-=2+b;
			printf (" ÷µ: %d",++len);
		} while(a>=0);
		
		/*
	int c = 0;
	
	while (c = getchar()!='') {
		switch (c - '2') {
			case 0: putchar(c+4);
			case 1: putchar(c+4);
			break;
			case 2: putchar(c+3);
			case 3: putchar(c+2);
			break;
			default:;
		}
		printf ("");
	}
		*/
		
		printf ("\n÷µ: %d",++len);
		return 0;
	}