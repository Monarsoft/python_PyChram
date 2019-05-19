class ForTest
{
	public static void main(String[] args) 
	{
		/*
			1. while 和 for 可以互换
			2. 格式上的不同，但是之间有些小差别
			3. 如果需要通过变量来循环进行控制，
				该变量只作为循环增量存在时，区别就体现出
		*/
		
		int i = 1;
		int sum = 0;
		while (i<=10)
		{
			sum +=i;
			System.out.println("i = "+i);
			++i;
		}
		System.out.println("sum = "+sum);

		for (int j = 1; j<=10; ++j)
		{
			System.out.println("sum = "+j);
		}

		//while and for 不同点 for循环结束后j的变量就被释放了

		System.out.println("Hello World!");
	}


	/*
		什么时候使用循环结构？
		1. 当某些代码执行多次时，使用循环结构完成。
		2. 当对一个条件进行一次判断时，可以使用if语句
		3. 当对一个条件进行多次判断时，可以使用while语句。
		
		注意：
			在使用循环时，一定要明确那些语需要参与循环，那些不需要参与循环
			循环通常情况下，需哟啊定义条件，需哟啊控制次数。
	
	*/
}
