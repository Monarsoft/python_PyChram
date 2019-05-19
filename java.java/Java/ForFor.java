public class ForFor {
	
	public static void main(String[] args) {
		
		int len = 6;
		
		for(int i = len; i>0; --i ) {
			for(int j = 0; j<=i; ++j) {
				System.out.print(" ");
			}
			System.out.println();
			
		} for (int t = 0; t<len; ++t) {
			for (int y = len; y>t; --y) {
				System.out.print(" " + y);
			}
			System.out.println();
		}
		System.out.println("\\aaaaa\\");
	} 
	
}