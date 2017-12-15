import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class StackOfStringArray {
	private String[] stack;
	private int capacity;
	private int count;
	public StackOfStringArray(int n) {
		capacity = n;
		count = 0;
		stack = new String[n];
	}
	public void push(String s) {
		// 1————>
		// if (count == capacity) throw new java.lang.IllegalArgumentException("stack is full"); 
		// else {
		//	stack[count+1] = s;
		//	count ++; 
		
		if (count >= capacity) throw new java.lang.IllegalArgumentException("stack is full"); 
		else {
			stack[count] = s;
			count ++;
		}
	}
	public String pop() {
		String s = stack[count-1];
		stack[count-1] = null;
		count --;
		return s;
	}
	public boolean isEmpty() {
		return count == 0;
	}
	public int size() {
		return count;
	}
 	public static void main(String[] args) {
        String s;
        StackOfStringArray stack = new StackOfStringArray(10);
        while (!StdIn.isEmpty()) {
                    s = StdIn.readString();
                    if (s.equals("-")) stack.pop(); // string.equals(string2);
                    else stack.push(s);
                }
        StdOut.println(stack.size());
    }
}