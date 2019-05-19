// 实现域名创建
class Realm_name {
	public static void main(String []args) {
		new Outer().name();// 这也相当于域名调用，没有对象！
		new Super2().show2();
	}
}
// 子类向上转型就会失去特有的方法！
class Outer {
	public void name() {
		new Object() {
			public void show() {
				System.out.println("域名 子类方法！ ");
			}
		}.show();
	}
}
// super
class Super1 {
	public void show1() {
		System.out.println("Super1 show1");
	}
}
class Super2 extends Super1 {
	int num = 99;
	public void show2() {
		//这里默认有个super(); 直接回到父类区执行有没有相同的方法,有就覆盖此类方法
		System.out.println("Super2 show2 : "+99);
	}
	public void sudu() {
		System.out.println("Sudu :"+num);
	}
}