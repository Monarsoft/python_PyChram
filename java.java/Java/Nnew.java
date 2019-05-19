package Nnew;
import new1.*;
class Nnew {
	public static void main(String []args) {
		New1 n = new New1();
		Thread t = new Thread(n);
		Thread t1 = new Thread(n);
		t.start();
		//t1.start();
		//n.run();
	}
}