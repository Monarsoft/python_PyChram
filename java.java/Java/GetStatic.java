 class GetStatic {
	public static void main(String [] args) {
		new GetStatic().gets();
		System.out.println(args);
		Res r = new Res();
		r.main1(args);
	}
	public void gets() {
		int args = 30;
		String colos = "Bulue";
		System.out.println(colos+":"+args);
	}
	
}

class PBEKey {
	static int age;
	static String name;
	public void person() {
 		System.out.println(name+age);
	}
}

 