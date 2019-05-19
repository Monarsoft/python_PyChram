/*
	使用同一个对象程序
*/
class New {
	public static void main(String []args) {
		Single ss = Single.index();
		Single sa = Single.index();
		System.out.println(sa == ss);
	}
}

class Single {
	static Single s = null;
	public static Single index() {
		if (s == null)
			s = new Single();
		return s;
	}
}