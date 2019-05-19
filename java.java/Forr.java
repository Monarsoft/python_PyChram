class Forrr
{
	public static void main(String[] atgs)
	{
		for (int i=0; i<10; i++)
		{
			for (int j=i; j<10; j++)
			{
				System.out.print(" i");
			}
			System.out.println();
		}

		for (int i=0; i<10; i++)
		{
			for (int t=0; t<i; t++)
			{
				System.out.print("*");
			}
			System.out.println();
		}

	}
}