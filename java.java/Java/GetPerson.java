  class GetPerson {
	public static void main(String []args) {
		/*Person Per = new Person(19,"Jack");
		Per.setNage();
		Per.setNage("\"( $ _ $ )\"",11);
		Per.setNage();
		*/
		Person p = new Person(21,"小明");
		Person p1 = new Person(211,"小强");
		
		p.setSame(p1);
		System.out.println(p.setSame(p1));
	}
}
	// Person Class
  class Person {
	private int age;
	private String name;
	
	Person(int age,String name) { //构造函数 ：创建对象时并调用
		if (age>0) {
			this.age = age;
			this.name = name;
			//son();
		}
		else System.out.println("Error : "+age);
	}
	
	public void setNage(String name, int age) {
		this.name = name;
		if (age>0) this.age = age;
	}
	
	public void setNage() {
		System.out.println("name :"+name+" "+age);
	}
		//比较是否同龄
	public boolean setSame(Person p) {
		/*if (this.age == p.age) return true;
			else	return false;*/
		return this.age == p.age;
	}
  }