/*
	继承中的升降类
*/
class INstanceof1 {
	public static void main(String []args) {
		final double PI = 3.14;
		meth(new Cat());
		Dongwu p = new Dog();	// 类型升级
		p.eat();

		Dog d = (Dog)p;
		d.guard();
		
		Dongwu c = d;
		c.eat();
		System.out.println(p.sun);
	}
	public static Dongwu meth(Dongwu d) {
		if(d instanceof Cat) { // instanceof 判断运算符
			Cat p = (Cat)d;
			p.grab();
		}
		return d;
	}
}
	// interface 接口类
interface a {
	
}
// 接口继承
class b implements a {
	
}

class Dongwu {
	int sun = 3;
	 void eat() {
		System.out.println("\b动物们 吃饭");
	}
	void go() {
		System.out.println("\b动物们 跑");
	}
}
class Cat extends Dongwu {
	void eat() {
		System.out.println("\b猫 吃鱼");
	}
	void grab() {
		System.out.println("\b捉老鼠");
	}
}
class Dog extends Dongwu {
	int sun = 4;
	 void eat () {
		System.out.println("\b啃骨头");
	}
	void guard() {
		System.out.println("\b守护家园");
	}
}