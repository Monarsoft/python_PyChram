class NewTest {
	public static void main(String []args) {
		//System.out.println("Hee Hee ");
		int len = a();
		//System.out.println(len);
		
	}
	public static int a() {
		int i=0;
		i++;
		///System.out.println("Hee Hee ");
		b();
		return i;
	}
	public static void b() {
		a();
	}
}