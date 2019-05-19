class ForForDemo
{
	public static void main(String[] args)
	{
		/*
		for (int i = 0; i<1; ++i)
		{
			for (int j = 0; j<10; ++j)
			{
				System.out.println("          *");
				System.out.println("         * *");
				System.out.println("        * * *");
				System.out.println("       * * * * ");
				System.out.println("      * * * * * ");
				System.out.println("     * * * * * *");
				System.out.println("    * * * * * * *");
				System.out.println("   * * * * * * * * ");
				System.out.println("  * * * * * * * * * ");
				System.out.println(" * * * * * * * * * * ");
				System.out.println("* * * * * * * * * * * ");
				System.out.println("       * * * * ");
				System.out.println("       * * * * ");
				System.out.println("       * * * * ");
				System.out.println("       * * * * ");
				System.out.println("       * * * * ");
				System.out.println("       * * * * ");
			}
		}*/
				
		for (int i=0; i<10; ++i)	  //外循环是控制行数
		{
			for (int j=0; j<10; ++j) //内循环是控制每行的列数
				System.out.print(" *");
			System.out.println();
		}
	}
}