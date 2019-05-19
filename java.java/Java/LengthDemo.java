class LengthDemo {
	public static void main(String []args) {
		int []array =  {6,5,4,1,2,3,0,7,8};
		
		for (int i= 0; i<array.length-1; i++) {
			for (int j = 1+i; j<array.length-1; j++) {
				if( array[i] > array[j] ) {
					array[i] = array[i] ^ array[j];
					array[j] = array[i] ^ array[j];
					array[j] = array[i] ^ array[j];
				}
			}
		}
		for (int i=0; i<array.length; i++) {
			System.out.print(" "+array[i]);
		}
	}
}