class WhileTest 
{
	public static void main(String[] args) 
	{
		int i, sum;
		i = 1;
		sum = 0;

		/*
			练习
			求出1-10之和
			思路
		*/
		while (i<=10)
		{
			sum +=i;
			++i;
		}
		
			System.out.println(sum);
		System.out.println("Hello World!");
	}
}
