/*
	extends �ô���
		1. ��ߴ���ĸ�����
		2. Ȼ��֮������˹�ϵ���������������ṩ��ǰ��
*/
class Static01 {
	public static void main(String []args) {
		Baby p = new Baby();
		Baby p1 = new Baby();
		Student t = new Student();
		p.Baby("С��",1);
		p1.Baby("����",2);
		t.study();
		t.person();
		
		System.out.println(args);
		return;
	}
}

// Person class
class Person {
	 int age;
	String name;
	 void person() {
		System.out.println("public person");
	}
}

// ����˸�����
class Baby extends Person { // Extends ��ϵ
	private int age;
	String name;
	public void person() {
		System.out.println(this.age+super.age+":\tpublic person");
	}
	
	public void Baby(String name, int age) {
		this.name = name;
		sry();
		name();
		return;
	} 
	static  void sry () {
		System.out.println("������...");
		return;
	}
	public void name() {
		System.out.println("name:"+this.name+"^"+age);
		System.out.println("----------------------------------------");
		return;
	}
}
// 	ѧ��
class Student extends Baby {
	void study() {
		name = "Student go to study start cmd";
		System.out.println(name);
	}
}