class Array06 {
	public static void main(String [] args) {
		
		int [] arr = {11,22,33,44,55,66,77,88,99};
		int Yes = getIndex(arr,77);
		System.out.println(Yes);
	}
	
	public static int getIndex(int [] arr, int key) {
		int max,min,mid;
		max  = arr.length;
		min = 0;
		mid = (max+min)>>1;
		
		while (key != arr[mid]) {
			if (arr[mid]>key) {
				max = mid-1;
			}
			else  {
				min = mid+1;
			}
			if (min>max) {
				return -1;
			}
			mid = (max+min)>>1;
		}	
		return mid;
	}
}