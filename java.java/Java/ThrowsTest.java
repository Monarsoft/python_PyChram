
class ThrowsTest {
	public static void main(String []args) {
		Car c = new CarBlue();
	}
}
interface Car {
	public  void brand();
}
class CarBlue {
	void CarBlue(String brand) {
		this.brand = brand;
	}
}