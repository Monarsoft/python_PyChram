 class Array05 {
	 public static void main(String[] args) {
		 
		 int [] arr = {3,25,4,8,56,734,5,234,12,54,36,54,7,56,43,5,32,4,2};
		 int ch = 8;
		 int res = res(arr,ch);
		 System.out.println("index = "+res);
	 }
	 // 数值查找 功能。
	public static int res(int [] arr, int ch) {
		for (int i=0; i<arr.length; ++i) {
			if (arr[i] == ch) 
				return i;
		}
		return -1;
	}
 }