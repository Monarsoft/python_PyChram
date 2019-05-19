/*
简单的排序工具 ，2017年11月19日 
@parman 1.0
*/
class Res {
	public static void main(String []args) {
		
	}
	public static void main1(String []args) {
		int [] arr = {6,5,4,2,1,3,0};
		getRes(arr);
		getRes1(arr);
		re(arr);
	}
	// 	 冒泡排序
	public static void getRes(int []arr) {
		for (int i=0; i<arr.length-1; i++) {
			for (int j=0; j<arr.length-1-i; j++) {
				if (arr[j]>arr[j+1]) {
					arr[j] = arr[j] ^ arr[j+1];
					arr[j+1] = arr[j] ^ arr[j+1];
					arr[j] = arr[j] ^ arr[j+1];
				}
			}
		}
	}
	//	查找排序
	 public static void getRes1(int []arr) {
		 for (int i=0; i<arr.length-1; i++) {
			 for (int j=0+i; j<arr.length; j++) {
				 if(arr[i]>arr[j]) {
					 arr[i] = arr[i] ^ arr[j];
					 arr[j] = arr[i] ^ arr[j];
					 arr[i] = arr[i] ^ arr[j];
				 }
			 }
		 }
	 }
	 //	输出
	 static void re(int []arr) {
		 for (int i=0; i<arr.length; i++) {
			 System.out.println(arr[i]);
		 }
	 }
 }