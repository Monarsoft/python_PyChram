class PersonDemo {
	public static void main(String []args) {
		person pe = new person();
		pe.getAge(9);
		int age = pe.getAge();
		System.out.println("AGe = "+age);
		
	}
}

class person {

		private int age;
		
		public void getAge(int a) {
			age = a;
		}
		public int getAge(){
			return age;
		}
	
	/*
		//ʵ���˵�����
	 private int age;  // private ˽�е� ��ָ�����иøı�
	public  void getAge(int a) {
		if (a>0 && a<130) {
			age = a;
			speak();
		}
		else
			System.out.println("age ... Error��");
		return a;
	}
	void speak() {
			System.out.println("age = "+age);
		}
*/
}