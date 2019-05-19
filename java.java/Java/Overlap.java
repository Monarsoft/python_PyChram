class Overlap {
	public static void main(String[] args) {
		stCFB();
		stCFB(8);
		
	}
	
	static void stCFB(int sum) {
		int[] ar = new int[10];
		for (int i=1; i<=sum; ++i) {
			for (int j=1; j<=i; ++j) {
				System.out.print(i+"*"+j+"="+i*j+"\t");
				ar[i] = i;
				System.out.print(ar[i]);
			}
			System.out.println();
		}
		return;
	}
			static void stCFB() {
				stCFB(9);
				return ;
			}
}