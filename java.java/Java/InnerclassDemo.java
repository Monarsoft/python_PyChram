class InnerclassDemo {
	void iner() {
		new Object() {
			void show() {
				System.out.println("Object iner");
			}
		}.show();
	}
	public static void main(String []args) {
		new InnerclassDemo().iner();
		new Out1().Demo();
	}
}
class Out1 {
	void Demo () {
		new Object() {
			void innter() {
				System.out.println("创建子类对象");
			}
		}.innter();// 创建一个简单的子类对象
	}
}