class Shpen {
	public static void main(String []args) {
		newashpen p = new newashpen();
		p.show();
	}
}

// 	覆盖的使用
//	何时使用 super
class ashpen {
	int nuber;
	void show() {
		System.out.println("show Nuber");
	}
}
/* 
	extends extends 继承　类X 通过extend 类Y来添加功能，或者添加变量，
	或者添加方法，或者覆盖类Y的方法。一个接口extends另外一个接口来添加方法。
*/
class newashpen extends ashpen {
	void show() {
		System.out.println("colc");
		System.out.println("naem");
		super.show();
	}
}