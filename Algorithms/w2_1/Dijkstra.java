import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class Dijkstra {

	public static void main(String[] args) {
		Stack<Double> value = new Stack<Double>();
		Stack<String> operand = new Stack<String>();
		String input, out;
		double inputValue, out1, out2, result;
		while (!StdIn.isEmpty()) {
			input = StdIn.readString();
			if (input.equals("(")) continue;
			else if (input.equals("+") || input.equals("-") || input.equals("*") || input.equals("／")) operand.push(input);
			else if (!input.equals(")")) {
				inputValue = Double.parseDouble(input);
				value.push(inputValue);
			}
			else if (input.equals(")")) {
				out1 = value.pop();
				out2 = value.pop();
				out = operand.pop();
				if (out.equals("+")) value.push((out1+out2));
				else if (out.equals("-")) value.push((out1-out2));
				else if (out.equals("*")) value.push((out1*out2));
				else if (out.equals("/")) value.push((out1/out2));
			}
		}
		result = value.pop();
		if (value.isEmpty() && operand.isEmpty()) StdOut.println(result);
		else StdOut.println("Wrong exprassion.");
	}
}