class Month 
{
	public static void main(String[] args) 
	{

		int Month;
		Month = 10;

	for (Month=1; Month<=12; ++Month)
	{
		if (Month>12||Month<1)
			System.out.println("无对应的季节:"+Month);
		else if (Month>=3&&Month<=5)
			System.out.println("3:5春季:"+Month);
		else if (Month>=6&&Month<=8)
			System.out.println("6:8夏季:"+Month);
		else if (Month>=9&&Month<=11)
			System.out.println("9:11秋季:"+Month);
		
		else 
			System.out.println("12:2冬季:"+Month);
			
		System.out.println("Hello World!");
	}

	}
}
