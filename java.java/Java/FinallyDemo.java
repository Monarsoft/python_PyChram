class FinallyDemo {
	public static void main(String []args) { 
		int []arr = new int[3];
		Rarry p = new Rarry();
		try {
			p.Rarry(arr,9);
		}
		catch (ArrayIndexOutOfBoundsException a) {
			System.out.println(a.toString());
				//System.exit(1);
		}

		finally {
			System.out.println("Finally");
			System.exit(0);
		}
	}
}

class Rarry  {
	void Rarry(int []arr,int superscript) {
		if(superscript<0 || superscript>arr.length) {
			throw new ArrayIndexOutOfBoundsException("�ű�Խ��:"+superscript);
		}
		if(superscript == arr.length) {
			throw new ArrayIndexOutOfBoundsException("����");
		}
		System.out.println(arr [superscript]);
	}
}