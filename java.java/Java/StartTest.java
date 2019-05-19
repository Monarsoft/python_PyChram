// 自定义线程
package mypackage;
class StartTest {
	public static void main(String []args) {
		Tests t = new Tests("零aaaaa");
		Tests t2 = new Tests(".壹..bbbb");

		t.start(); // 开启线程 ，调用run方法
		t2.start();		
		//t.run();
		t2.run();
	}
}
class Tests extends Thread {
	String na;
	Tests(String na) {
		//this.na = na;
		super(na); // 给线程传名字
	}
	public void run() {
		for (int i=0; i<6; i++) {
			for (int j = -999999999; j<999999999; j++) {}
			System.out.println("....."+na+" "+Thread.currentThread().getName());
		}
	}
}

// 调用run方法和调用start方法的区别。
// 1.调用run方法： 不能开启线程 ，直接使用 主线程执行
// 2.调用start 方法：开启线程 ，调用run 方法 