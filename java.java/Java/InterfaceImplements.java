class  InterfaceImplements {
	public static void main(String []args) {
		D p = new D();
		
		System.out.println(p.PI);
		p.go();
		System.out.println(Walk.PI);
		System.out.println(D.PI);
		p.goo();
	}
}
// Interface 
interface Walk {
	public static final double PI = 3.14;
	
	public abstract void go();
	public abstract void goo();
}
// implemends
class D implements Walk{
	public void go() {
		System.out.println("Walk: go");
	}
	public void goo() {
		System.out.println("Walk: goo");
	}
}
