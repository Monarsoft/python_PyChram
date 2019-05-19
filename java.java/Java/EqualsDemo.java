// integer.tohexString();
class Demo {
	int age = 100;
	void Demo(int age) {
		this.age = age;
	}
	
	public boolean equals(Object obj) {
		if (!(obj instanceof Demo)) {
			throw new ClassCastException("类型不一致:"+obj);
			//System.out.print("不相同的类型:");
			//return false;
		}
		Demo p = (Demo)obj;
		return this.age == p.age;
	}
}

class Of {
	
}  

class EqualsDemo {
	public static void main(String []args) {
		Demo d = new Demo();
		//Demo p = new Demo();
		Of p  = new Of();
		System.out.println(d.equals(p));
		
	}
}