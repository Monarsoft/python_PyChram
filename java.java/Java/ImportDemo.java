package Demo;
import Test.*; // 包导入 ，为了简写
class ImportDemo {
	public static void main(String []args) {
		//Test.ImportTest i = new Test.ImportTest();  // 未使用IMpor前写法
		ImportTest i = new ImportTest(); // 简写
		i.Stub();
	}
}