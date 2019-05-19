class Array07 {
	public static void main(String [] args) {
		toHex(60);
	}
	
	public static void toHex(int num) {
		for (int x=0; x<8; x++) {
			int temp = num & 15;
			if (temp>9)
				System.out.print((char)(temp-10+'A')+"   ");
			else
				System.out.print(temp);
			num = num >>> 4;
		}
	}
} 