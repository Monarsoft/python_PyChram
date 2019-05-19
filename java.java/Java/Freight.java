class Freight {
	static void add(double i, int j) {
		System.out.println("double , int");
	}
	static void add(int i, double j) {
		System.out.println("int , double");
		
	}
	public static void main(String []args) {
		add(6,1.0);
		add(9.2,6);
	}
}