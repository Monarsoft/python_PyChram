public class For99 {
	public static void main(String[] arags) {
		
		for (int i = 1; i<10; ++i) {
			for (int j = 1; j<=i; ++j) {
				System.out.print(i + "*" + j + "=" + i*j + "\t");
			}
			
			System.out.println();
		}
	}
}