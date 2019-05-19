public class ForTest02 {
	public static void main(String[] args) {
		
		System.out.println("----------------------------------------------------------------------");
		System.out.println("----------------------------------------------------------------------");
		for(int a1 =0; a1<10; ++a1) {
			for(int a3 = 0; a3<=4; ++a3) {
				System.out.print(" ");
			}
			for(int a2 = 0; a2<5; ++a2) {
				System.out.print("* ");
			}
			for(int a4 = 0; a4<25; ++a4) {
				System.out.print(" ");
			}
			for(int a5 = 0; a5<5; ++a5) {
				System.out.print("* ");
			}
			System.out.println();
		}
		
		for(int i = 0; i<10; ++i ) {
			for(int j = 0; j<i; ++j) {
				System.out.print(" ");
			}
			for(int z = i; z<10; ++z) {
				System.out.print("* ");
			}
			for(int y = 0; y<i; ++y) {
				System.out.print("");
			}
			for (int a6 = 0; a6<13; ++a6) {
				System.out.print(" ");
			}
			for(int a7 = 0; a7<=i; ++a7) {
				System.out.print("  ");
			}
			for(int a8 = i; a8<10; ++a8) {
				System.out.print("* ");
			}
			System.out.println();
		}
		System.out.println("---------------------------------------------------------------------");
		System.out.println("---------------------------------------------------------------------");
	}
}