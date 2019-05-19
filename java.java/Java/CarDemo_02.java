class CarDemo_02 {
	public static void main(String []args) {
		Car c1 = new Car();
		
		show(c1,"Green!");
		c1.run();
	}
	
	public static void show(Car c, String color) {
		c.num = 8;
		c.color = color;
	}
}
class Car {
	int num;
	String color;
	void run() {
		System.out.println(num+"..."+color);
	}
}