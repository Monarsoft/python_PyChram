class CarTes {
	public static void main(String [] agers) {
		Car cat = new Car ();
		
		cat.getcar(1,"Blue");
		int sun = cat.getcar();
		System.out.println(sun);
	}
}
/*
/*
	Car车图纸功能  4 个好处：复用性 安全性 便于使用 将变化隔离
	private :私有(隐藏属性)，是一个权限修饰符。用于修饰成员 
	注意：私有仅仅是封装的一种体现而已
 私有的一定是封装的 ，但封装的不一定是私有的
 */
class Car {
	private int sun;  // 私有
	String color;
	
	public void getcar(int s, String c) {
		if (s>3 && s<100) {
			sun = s;
			color = c;
		}
		else System.out.println("数据错误！");
	}
	 public int getcar() {
		System.out.print("Car: "+color+" ^ ");
		return sun;
	}
}