 package ProtectedTest;
 import Test.*; // ������  // ֱ��ʹ����
class ProtectedTest {
	public static void main(String []args) {
		TestDTM1 p = new TestDTM1();
		p.start();
		Test1 t = new Test1();
	}
}
class TestDTM1 extends Test.Test1 {
	 TestDTM1() {
		Test1();
	}
}