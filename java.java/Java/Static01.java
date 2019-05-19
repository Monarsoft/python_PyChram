/*
	extends 好处：
		1. 提高代码的复用性
		2. 然类之间产生了关系，给第三个特征提供了前提
*/
class Static01 {
	public static void main(String []args) {
		Baby p = new Baby();
		Baby p1 = new Baby();
		Student t = new Student();
		p.Baby("小娟",1);
		p1.Baby("宝贝",2);
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

// 提高了复用性
class Baby extends Person { // Extends 继系
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
		System.out.println("哇哇哇...");
		return;
	}
	public void name() {
		System.out.println("name:"+this.name+"^"+age);
		System.out.println("----------------------------------------");
		return;
	}
}
// 	学生
class Student extends Baby {
	void study() {
		name = "Student go to study start cmd";
		System.out.println(name);
	}
}