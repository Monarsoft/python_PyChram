public class BreakContinueDemo {
	public static void main(String[] args) {
		
		 bfor:for (int i = 0; i<3; ++i) {
			for (int j = 0; j<3; ++j) {
				System.out.println("Hello Break and Continue Demo!");
				if (i%2 == 0) break bfor; //终止外循环
				continue bfor; //回到外部循环
			}
		}

	}
} 
/*
19点34分 2017年10月31日 输出结果
	------------------------------------------------------------------------------------------
	
	Hello Break and Continue Demo!
	
	------------------------------------------------------------------------------------------
*/