// �Զ����߳�
package mypackage;
class StartTest {
	public static void main(String []args) {
		Tests t = new Tests("��aaaaa");
		Tests t2 = new Tests(".Ҽ..bbbb");

		t.start(); // �����߳� ������run����
		t2.start();		
		//t.run();
		t2.run();
	}
}
class Tests extends Thread {
	String na;
	Tests(String na) {
		//this.na = na;
		super(na); // ���̴߳�����
	}
	public void run() {
		for (int i=0; i<6; i++) {
			for (int j = -999999999; j<999999999; j++) {}
			System.out.println("....."+na+" "+Thread.currentThread().getName());
		}
	}
}

// ����run�����͵���start����������
// 1.����run������ ���ܿ����߳� ��ֱ��ʹ�� ���߳�ִ��
// 2.����start �����������߳� ������run ���� 