// ʵ��Walk�������
class Abstract01 {
	public static void main(String []args) {
		superman p = new superman();
		p.go();
	}
}
// ӵ�����������
 abstract class Walk {
	abstract void go() ; // ���кܶ���
}
// ����
class person extends Walk {
	void go() {
		System.out.println("person: Wald");
	}
}
// ��������
class superman extends Walk{
	void go() {
			System.out.println("superman: Wald");
	}
}