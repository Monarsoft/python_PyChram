// super �÷�
class Realm_name2 {
	public static void main(String []args) {
		new Zi().show(); // new һ��Zi�࣬����ִ�й��캯��
	}
}

 class Fu {
	Fu() {
		show(); �����е�����show����
	}
	void show() {// �����﷢����������÷�����ֱ��ִ������show����
		System.out.println("heheh");
	}
}
class Zi extends Fu{ // extends �Ǽ̳�
	int num = 99; // ��ʾ��ʼ�����ڹ��캯��֮�󣬲���99��
	Zi() {
		//�����и�super(); ֱ�ӵ�������ִ�и����й��췽�����֣�
		System.out.println("Zi �෽�� ��"+num);
	}
	void show() {
		System.out.println("Zi show :"+num);
	}
}