package new1;
public class New1 implements Runnable {
	public void run() {
		main();
		//System.out.println("NClob run");
	}
	public  void main() {
		int nn = 100;
		 for(int i=0; i<nn; i++){
			System.out.println(Thread.currentThread().getName()+"......"+nn--);
		}
		System.out.println("Nwq"+Thread.currentThread().getName());
	}
}