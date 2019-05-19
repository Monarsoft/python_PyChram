 class Test01 {
	 public static void main(String []args) {
		 
			Test(10);
	 }
	 
	 public static void Test(int arr) {
		 
		 for (int i=0; i<arr; i++) {
			 for(int a=arr; a>i; a--) {
				 System.out.print(" ");
			 }
		for (int b=0; b<=i; b++) { 
			if (i== 0 || b==i)
			System.out.print("* ");
		else 
			System.out.print("* ");
		 }
		if (i!=0 || i!=arr)
			System.out.print(" ");
		else
			 System.out.println();
		 }
		 
		 return;
	 }
 }