// ʵ����������
class Realm_name {
	public static void main(String []args) {
		new Outer().name();// ��Ҳ�൱���������ã�û�ж���
		new Super2().show2();
	}
}
// ��������ת�;ͻ�ʧȥ���еķ�����
class Outer {
	public void name() {
		new Object() {
			public void show() {
				System.out.println("���� ���෽���� ");
			}
		}.show();
	}
}
// super
class Super1 {
	public void show1() {
		System.out.println("Super1 show1");
	}
}
class Super2 extends Super1 {
	int num = 99;
	public void show2() {
		//����Ĭ���и�super(); ֱ�ӻص�������ִ����û����ͬ�ķ���,�о͸��Ǵ��෽��
		System.out.println("Super2 show2 : "+99);
	}
	public void sudu() {
		System.out.println("Sudu :"+num);
	}
}