class Array04 {
	public static void main(String[] args) {
		
		int [] arr = {6,5,7,89,5,4,32,1,1,0,};
		Myprint(arr);
		selecit(arr);
		Myprint(arr);
	}
	
	public static void selecit(int [] arr) {
		for (int i=0; i<arr.length-1; ++i) {
			for (int j=0; j<arr.length-1-i; ++j) {
				if (arr[j]>arr[j+1]) {
					arr[j] = arr[j]^arr[j+1];
					arr[j+1] = arr[j]^arr[j+1];
					arr[j] = arr[j]^arr[j+1];
				}
			}
		}
	}
	
	// Êä³ö½á¹û
	public static void Myprint(int [] arr) {
		for (int i=0; i<arr.length; ++i) {
			System.out.print(" "+arr[i]);
		}
		System.out.println();
	}
}