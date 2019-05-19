public class ZiZeng
{
	public static void main(String[] args)
	{
		int a = 6;
		a = ++(--a)++; 
		System.out.println(a);
		try{
			InputStreamReader is = new InputStreamReader (System.in);
		}catch(Exception e)

	}
}
//----------------------------------------------------
/*
	//输出结果：
ZiZeng.java:6: 错误: 意外的类型
                a = ++(--a)++;
                       ^
  需要: 变量
  找到:    值
1 个错误

*/