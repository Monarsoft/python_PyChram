class CarDemo_01 {
	public static void main(String []args) {
		Car c = new Car();
		Car e = new Car();
		c = e;
		// 下面的赋值并不是给类当中的属性赋值，而是给这个对象的属性 赋值
		e.sum = 4;
		c.color = "Red";
		
		e.rum();
	}
}
//这里相当于Car的图纸共有的属性而已
class Car {
	int sum;
	String color;
	void rum() {
		System.out.println(sum+"..."+color);
	}
}

/*
	//输出结果为：
-----------------------------------------------------------
	4...Red
-----------------------------------------------------------
*/