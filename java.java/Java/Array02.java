class Array02 {
	public static void main(String[] args) {
		
		int [] arr = new int [100];
		
		for (int x=1; x<arr.length; ++x) {
			arr[x] = x;
		}
		int max = getMax(arr);
		System.out.print("MAX =  "+max);
		
		return ;
	}
	
	public static int getMax(int [] arr) {
		int max = 0;
		for (int i = 1; i<arr.length; ++i) {
			if (arr[i] > arr[max]) {
				max = arr[i];
			}
		}
		return max;
	}
}