/*
	��ʦ����
*/
class StudyTest2 {
	public static void main(String []args) {
		Teacher teach = new Teacher();
		teach.prelect("Wang Sir");
	}
}
// ��ʦ����
class Teacher {
	private String name;
	private Computer comp;
	public void  prelect(String name) {
		this.name = name;
		comp = new Computer();
		if(true) {
			comp.run();
		}
		System.out.println("����"+name);
	}
}
// ���ε���
class Computer  {
	private int state = 0;
	public void run() {
		if(state == 1) {
			//throw new LanpingException("��������");
		}
		System.out.println("��������");
		Lanping lg = new Lanping("A");
	}
}

class LanpingException extends Exception {
	
	LanpingException(String msg) {
		super(msg);
	}
}