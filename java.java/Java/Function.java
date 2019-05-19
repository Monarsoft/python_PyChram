class Function {
	public static void main(String[] args) {
		
		int a = myprint(6);
		System.out.println(a);
		
		System.out.print(ch(0));
	}
	static int myprint(int len) {
		
		for (int i=0; i<len; ++i) {
			len +=i;
			System.out.println(len);
			if (i%2 != 0) break;
		}
		return len;
	}
	static char ch(int i) {
		char ch;
		if (i == 65) ch = 'A';
		else if (i == 66) ch = 'B';
		else ch = 'C';
		return ch;
	}
}