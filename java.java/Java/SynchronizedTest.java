class SynchronizedTest {
	public static void main(String []args) {
		Bank b = new Bank();
		Thread t = new Thread(b);
		Thread c  = new Thread(b);
		c.start();
		t.start();
	}
}
class Xun {
	public synchronized void add(int sum) {
		int sun = 0;
			sun = sun + sum;
			System.out.println(".."+sun);	
	}
}
class Bank implements Runnable {
		Xun x = new Xun();
		public void run() {
		for (int i=0; i<3; i++) {
			x.add(100);
		}
	}
}