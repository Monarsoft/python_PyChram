/*
	作者：LianYong
	日期：2017年10月26日
	功能：判断两个数是否能整除
*/

public class Demo
{
	public static void main(String[] args)
	{
		int a = 2;
		int b = 4;
		if(b%a == 0)
		{
			System.out.println(b+"能被"+a+"整除");
		}
		else
		{
			System.out.println(b+"不能被"+a+"整除");
		}
	}
}