class ThrowsTestDemo {
	public static void main(String []args) {
		Feanly p = new Feanly();
		p.shor();
		Rdn n = new Rdn(6);
		n.multiplication();
	}
}
interface Ang {
	public void shor();
}
class Feanly implements Ang  {
	public void shor() {
		 System.out.println("go()");
	}
}
class Rdn {
	int len = 0;
	Rdn (int len) {
		if(!(len<0)) {
			this.len = len;
		}
		else throw new Exception();
	}
	void multiplication() {
			for (int i=1; i<=len; i++) {
				for (int j=1; j<=i; j++) {
					System.out.print("\t");
					System.out.print(j+"*"+i+"="+i*j);
				}
				System.out.println();
			}
	}
}