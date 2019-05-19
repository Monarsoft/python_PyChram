// super 用法
class Realm_name2 {
	public static void main(String []args) {
		new Zi().show(); // new 一个Zi类，首先执行构造函数
	}
}

 class Fu {
	Fu() {
		show(); 父类中调用了show方法
	}
	void show() {// 到这里发现是子类调用方法，直接执行子类show方法
		System.out.println("heheh");
	}
}
class Zi extends Fu{ // extends 是继承
	int num = 99; // 显示初始化是在构造函数之后，才是99。
	Zi() {
		//这里有个super(); 直接到父类中执行父类中构造方法发现，
		System.out.println("Zi 类方法 ："+num);
	}
	void show() {
		System.out.println("Zi show :"+num);
	}
}