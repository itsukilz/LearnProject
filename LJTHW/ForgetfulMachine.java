import java.util.Scanner;

public class ForgetfulMachine {
	public static void main ( String[] args) {
		Scanner keyboard = new Scanner(System.in);

		System.out.println( "What city is the capital of France?" );
		String p = keyboard.next();
		System.out.println( "I think maybe " + p + " is the capital of France.");
		
		System.out.println( "What is your age?" );
		int age = keyboard.nextInt();
		System.out.println( "I am " + age + " years old.");

		System.out.println( "What is pi?" );
		double pi = keyboard.nextDouble();
		System.out.println( "pi is " + pi + ".");
	}
}