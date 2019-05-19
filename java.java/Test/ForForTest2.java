class ForForTest2 
{
	public static void main(String[] args) 
	{
		int len = 30;

		for (int i=0; i<18; i++)
		{
			for (int j=i; j<18; j++)
			{
				System.out.print(".");
			}
			for (int t=0; t<i; t++)
			{
				System.out.print(" $");
			}
			for (int k=i; k<18; k++)
			{
				System.out.print(" ");
			}
			System.out.println();
		}

		for (int y=0; y<18; y++)
				{
					for (int a=0; a<y; a++)
					{
						System.out.print(".");
					}
					for (int c=y; c<18; c++)
					{
						System.out.print(" $");
					}
					for (int g=y; g<18; g++)
					{
						System.out.print(".");
					}

					System.out.println();
				}
		System.out.println("Hello World!");
	}
}
