/*
	老师用CP上课
	*/
class StudyTest {
	public static void main(String []args) {
		Teacher t = new Teacher ("Wang Sir");
		t.prelect();
	}
}
class Teacher {
	private String name;
	private Computer comp;
	Teacher (String name) {
		this.name = name;
		comp = new Computer("DaeR");
	}
	public void prelect() {
		comp.run();
		System.out.println("讲课"+name);
	}
}
class Computer {
	private String plate;
	Computer(String plate) {
		this.plate = plate;
	}
	public void run() {
		System.out.println("Supter source on "+plate);
	}
}