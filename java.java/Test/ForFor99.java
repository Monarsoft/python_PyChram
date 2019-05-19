class ForFor99
{
	public static void main(String[] args)
	{
		int a, t;

		for (int i=1; i<=9; i++)
		{
			for (int j=1; j<=i; j++)
			{
				System.out.print(j+"*"+i+"="+(j*i)+"\t");
			}
			System.out.print("\n");
		}
	}
}
	/*
		/n 回车:
		/t 制表符
		/b 退格
		/r 按一下回车键

		Windows系统中回车符其实就是由两个符号组成的 /r/n
		Linux系统中回车符是/n
	*/