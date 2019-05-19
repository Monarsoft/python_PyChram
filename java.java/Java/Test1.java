package Test;
public class Test1 extends Thread {
	protected void Test1() {
		System.out.println("Test1");
		System.out.println("Test a");
	}
	void run () {
		System.out.println("Thread run ");
	}
}