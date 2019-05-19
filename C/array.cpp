#include <stdio.h>
#include <windows.h>

int main(int argc, char *argv[])
{
	int arry[] = {5,4,3,6,1,2,7,9,8,0};
	int len = sizeof(arry)/sizeof(int);

	for (int i=0;i<len-1 ;i++ )
	{
		for (int j=i+1;j<len-i-1 ;j++ )
		{
			if (arry[i]>arry[j])
			{
				arry[i] = arry[i]^arry[j];
				arry[j] = arry[i]^arry[j];
				arry[i] = arry[i]^arry[j];
			}
		}
	}
	for (int n=0;n<len ;n++ )
	{
		printf("%d ", arry[n]);
	}

	//system("pause");
	return 0;
}
