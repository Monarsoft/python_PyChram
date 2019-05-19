class BreakContinueDemo
{
	public static void main(String[] args) 
	{
	/*	
			break: 跳出
			break作用范围：要么是switch语句，要么是循环语句。
			记住： 当break跳出所在的单前循环。
					如果出现了循环渠道
		for (int x=0; x<3; x++)
		{
			if (x==1)
			{
				break;
				System.out.println("x = "+x);
			}
		}*/
//---------------------------------------------------------------
		zhangshan:for (int i=0; i<3; i++)
		{
			for (int j=0; j<3; j++)
			{
				System.out.println("i = "+i);
				break zhangshan;
			}
		}

//---------------------------------------------------------------
		/*
			continue:继续
			作用范围：循环结构。
			continue：结束本次循环，继续下次循环。
			如果continue单独存在时， continue下面不要有任何语句，应为执行不到
		*/
	for (int x=0; x<3; x++)
	{
		if (x%2==0)
			continue;		
		System.out.println("x = "+x);
	}

		System.out.println("Hello World!");
	}
}
