public class Array03 {
	
	public static void main(String[] args) {
		int [] arr = {1,3,2,4,6,9,8,5,6,0};
		
		Myprint(arr);
		selecit (arr);
		effervesce(arr);
		Myprint(arr);
		
		return ;
	}
	
	public static void swap(int [] arr, int i, int j) {
		arr[i] = arr[i]^arr[j];
		arr[j] = arr[i]^arr[j];
		arr[i] = arr[i]^arr[j];
	}
	
	public static void effervesce(int [] arr) {
		for (int i=0; i<arr.length-1; ++i) {
			for (int y=0; y<arr.length-1-i; ++y) {
				if (arr[y]>arr[y+1]) {
					swap(arr,y,y+1);
				}
			}
		}
		return;
	}
	
	public static void selecit(int [] arr) {
		
		for(int i=0; i<arr.length-1; ++i) {
			for (int j=i+1; j<arr.length; ++j) {
				if (arr[i]>arr[j]) {
					swap(arr,i,j);
				}
			}
		}
		return ;
	}
	public static void Myprint(int [] arr) {
		for(int x = 0; x<arr.length; ++x) {
			System.out.print(" "+arr[x]);
		}
		System.out.println();
	}
}