class Rfz {
	public static void main(String []args) {
		
		Zi p = new Zi();
		p.res();
		System.out.println(args);
	}
}
class H extends Object /* Ä¬ÈÏÓĞ¸öObje*/ {
	int it;
	H(int x) {
		System.out.println("OK"+x);
		return;
	}
	void res() {
		int i =100;
		System.out.println(i);
		System.out.println("World");
	}
}

class Fu extends H {
	int it = 11;
	Fu(int x) {
		super(1);
		System.out.println("FU"+x);
		return;
	}
	void res() {
		int it = 10;
			System.out.println("¸²¸Ç");
			//res();
		}
}
class Zi extends Fu {
	int it = 10;
	Zi() {
		super(8);
		System.out.println(super.it);
		return;
	}
}