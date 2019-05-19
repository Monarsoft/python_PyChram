// 实现Walk这个功能
class Abstract01 {
	public static void main(String []args) {
		superman p = new superman();
		p.go();
	}
}
// 拥有走这个功能
 abstract class Walk {
	abstract void go() ; // 走有很多类
}
// 人类
class person extends Walk {
	void go() {
		System.out.println("person: Wald");
	}
}
// 其它物种
class superman extends Walk{
	void go() {
			System.out.println("superman: Wald");
	}
}