class Shpen {
	public static void main(String []args) {
		newashpen p = new newashpen();
		p.show();
	}
}

// 	���ǵ�ʹ��
//	��ʱʹ�� super
class ashpen {
	int nuber;
	void show() {
		System.out.println("show Nuber");
	}
}
/* 
	extends extends �̳С���X ͨ��extend ��Y����ӹ��ܣ�������ӱ�����
	������ӷ��������߸�����Y�ķ�����һ���ӿ�extends����һ���ӿ�����ӷ�����
*/
class newashpen extends ashpen {
	void show() {
		System.out.println("colc");
		System.out.println("naem");
		super.show();
	}
}