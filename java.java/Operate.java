class Operate 
{
	public static void main(String[] args) 
	{
		int i, j;
		i =6;
		j =1;

		System.out.println("i = "+i+",j = "+j);
		
		i = i ^ j;	// 6 ^ 1
		j = i ^ j;	//(6 ^ 1) ^ 1 = 6;
		i = i ^ j;	//(6 ^ 1) ^ 6 = 1;


		System.out.println("i = "+i+",j = "+j);
		
		System.out.println("Hello World!");
	}
}
