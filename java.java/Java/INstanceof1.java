/*
	�̳��е�������
*/
class INstanceof1 {
	public static void main(String []args) {
		final double PI = 3.14;
		meth(new Cat());
		Dongwu p = new Dog();	// ��������
		p.eat();

		Dog d = (Dog)p;
		d.guard();
		
		Dongwu c = d;
		c.eat();
		System.out.println(p.sun);
	}
	public static Dongwu meth(Dongwu d) {
		if(d instanceof Cat) { // instanceof �ж������
			Cat p = (Cat)d;
			p.grab();
		}
		return d;
	}
}
	// interface �ӿ���
interface a {
	
}
// �ӿڼ̳�
class b implements a {
	
}

class Dongwu {
	int sun = 3;
	 void eat() {
		System.out.println("\b������ �Է�");
	}
	void go() {
		System.out.println("\b������ ��");
	}
}
class Cat extends Dongwu {
	void eat() {
		System.out.println("\bè ����");
	}
	void grab() {
		System.out.println("\b׽����");
	}
}
class Dog extends Dongwu {
	int sun = 4;
	 void eat () {
		System.out.println("\b�й�ͷ");
	}
	void guard() {
		System.out.println("\b�ػ���԰");
	}
}