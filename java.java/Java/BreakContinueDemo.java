public class BreakContinueDemo {
	public static void main(String[] args) {
		
		 bfor:for (int i = 0; i<3; ++i) {
			for (int j = 0; j<3; ++j) {
				System.out.println("Hello Break and Continue Demo!");
				if (i%2 == 0) break bfor; //��ֹ��ѭ��
				continue bfor; //�ص��ⲿѭ��
			}
		}

	}
} 
/*
19��34�� 2017��10��31�� ������
	------------------------------------------------------------------------------------------
	
	Hello Break and Continue Demo!
	
	------------------------------------------------------------------------------------------
*/