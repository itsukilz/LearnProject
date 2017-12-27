import java.util.Scanner;

public class ForgetfulMachine {
	public static void main ( String[] args) {
		Scanner keyboard = new Scanner(System.in);

		System.out.println( "What city is the capital of France?" );
		String p = keyboard.next();
		System.out.println( "I think maybe " + p + " is the capital of France.");
	}
}