/*
	老师讲课
*/
class StudyTest2 {
	public static void main(String []args) {
		Teacher teach = new Teacher();
		teach.prelect("Wang Sir");
	}
}
// 老师讲课
class Teacher {
	private String name;
	private Computer comp;
	public void  prelect(String name) {
		this.name = name;
		comp = new Computer();
		if(true) {
			comp.run();
		}
		System.out.println("讲课"+name);
	}
}
// 讲课电脑
class Computer  {
	private int state = 0;
	public void run() {
		if(state == 1) {
			//throw new LanpingException("电脑蓝屏");
		}
		System.out.println("电脑启动");
		Lanping lg = new Lanping("A");
	}
}

class LanpingException extends Exception {
	
	LanpingException(String msg) {
		super(msg);
	}
}