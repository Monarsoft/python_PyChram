class CarTes {
	public static void main(String [] agers) {
		Car cat = new Car ();
		
		cat.getcar(1,"Blue");
		int sun = cat.getcar();
		System.out.println(sun);
	}
}
/*
/*
	Car��ͼֽ����  4 ���ô��������� ��ȫ�� ����ʹ�� ���仯����
	private :˽��(��������)����һ��Ȩ�����η����������γ�Ա 
	ע�⣺˽�н����Ƿ�װ��һ�����ֶ���
 ˽�е�һ���Ƿ�װ�� ������װ�Ĳ�һ����˽�е�
 */
class Car {
	private int sun;  // ˽��
	String color;
	
	public void getcar(int s, String c) {
		if (s>3 && s<100) {
			sun = s;
			color = c;
		}
		else System.out.println("���ݴ���");
	}
	 public int getcar() {
		System.out.print("Car: "+color+" ^ ");
		return sun;
	}
}