class CarDemo_01 {
	public static void main(String []args) {
		Car c = new Car();
		Car e = new Car();
		c = e;
		// ����ĸ�ֵ�����Ǹ��൱�е����Ը�ֵ�����Ǹ������������� ��ֵ
		e.sum = 4;
		c.color = "Red";
		
		e.rum();
	}
}
//�����൱��Car��ͼֽ���е����Զ���
class Car {
	int sum;
	String color;
	void rum() {
		System.out.println(sum+"..."+color);
	}
}

/*
	//������Ϊ��
-----------------------------------------------------------
	4...Red
-----------------------------------------------------------
*/