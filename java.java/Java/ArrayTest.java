class ArrayTest {
	public static void main(String [] ars) {
		
		int [] arr ={1,3,5,6,7,8,9};

		int len = ArrayTes (arr, 3);
		System.out.println(len);
		
		return ;
	}
	
	public static int  ArrayTes (int [] arr, int Tes) {
		
		int max,min,mid;
		max = arr.length;
		min = 0;
		mid = (max + min)/2;
		
		while (arr[mid] != Tes) {
			if (arr[mid] > Tes) {
				max = mid -1;
			}
			else if (arr[mid] < Tes) {
				min = mid +1;
			}
			else {
				mid = (max+min)/2;
			}
			return -1;
		}
		return arr[mid];
	}
}