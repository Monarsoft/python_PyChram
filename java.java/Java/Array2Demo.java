 class Array2Demo {
	 public static void main(String []args){
		 
		 int [][] array = new int [3][6];
		 Dog det = new Dog();
		 array[2][1] = 4;
		 System.out.println(array); // [[I@15db9742  @ 左边是实体的类型，右边是实体的哈希值(地址标号)
		 System.out.println(array[0]); // [I@6d06d69c
		 System.out.println(array[0][0]); // 0
		 //System.out.println(array[2][1]);// 打印二维数组中的角标为2的一维数组角标中为1的元素。
		 arr(array,3,6);
		 det.GetSun(6);
		 System.out.println(det.GetSun());
		 System.out.println(det.GetColor("yellow"));
		 
		 return;
	 }
	 public static void arr(int [][] array, int i1,int j1) {
		 for (int i=0; i<i1; i++) {
			 for (int j=0; j<j1; j++) {
				 //System.out.print("!"+j+"!");
				 System.out.print(array[i][j]);
			 }
			 System.out.println();
		 }
	 }
 }
 class Dog {
	 private  int sun;
	 private String color;
	 public   void GetSun(int su) {
		 if (su == 4) {
			 sun = su;
		 }
		 else {
			 System.out.print("Error!");
		 }
	 }
	 public  int GetSun() {
		 return sun;
	 }
	 
	 public  String GetColor(String c) {
		color = c;
		return color;
	 }
	 
 }