class ForTest
{
	public static void main(String[] args) 
	{
		/*
			1. while �� for ���Ի���
			2. ��ʽ�ϵĲ�ͬ������֮����ЩС���
			3. �����Ҫͨ��������ѭ�����п��ƣ�
				�ñ���ֻ��Ϊѭ����������ʱ����������ֳ�
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

		//while and for ��ͬ�� forѭ��������j�ı����ͱ��ͷ���

		System.out.println("Hello World!");
	}


	/*
		ʲôʱ��ʹ��ѭ���ṹ��
		1. ��ĳЩ����ִ�ж��ʱ��ʹ��ѭ���ṹ��ɡ�
		2. ����һ����������һ���ж�ʱ������ʹ��if���
		3. ����һ���������ж���ж�ʱ������ʹ��while��䡣
		
		ע�⣺
			��ʹ��ѭ��ʱ��һ��Ҫ��ȷ��Щ����Ҫ����ѭ������Щ����Ҫ����ѭ��
			ѭ��ͨ������£���Ӵ��������������Ӵ�����ƴ�����
	
	*/
}
