class WhileTest2 
{
	public static void main(String[] args) 
	{

			/*
			练习
			1-100,6倍数个数

			思路：
			1. 定义一个变量用于做运算
			2. 做一个判断1-100 之间每个数除以6的与是否为零，如果是则定义一个变量自增一下
				就能知道有多少个能被6整除的
			3. 每次做运算的值也得自增，所以得用循环结构， 还要进行判断
		*/

		int i, number;
		i = 1;
		number= 0;

		while (i<=100)
		{
			if (i%6==0)
				number++;
			i++;
		}		
		
		System.out.println("number = "+number);
		System.out.println("Hello World!");
	}
}
