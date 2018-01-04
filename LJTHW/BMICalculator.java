import java.util.Scanner;

public class BMICalculator {
	public static void main (String[] args) {
		Scanner keyboard = new Scanner(System.in);
		double m, kg, bmi;

		System.out.print("Your weight in kg: ");
		kg = keyboard.nextDouble();

		System.out.print("Your height in m: ");
		m = keyboard.nextDouble();

		bmi = kg / (m*m);
		System.out.print("Your BMI is "+bmi);
	}
}