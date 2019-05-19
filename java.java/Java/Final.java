/*
	Final关键字的使用
*/
class Final {
	public static void main(String []args) {
		Zi z = new Zi();
	}
}

class Fu {
	 void method() {
		// 使用关键字 final 的变量不可以改变 ，变量名需以大写表示常量
		 final double MY_PI = 3.14; 

	} 
}
class Zi extends Fu {
	
}