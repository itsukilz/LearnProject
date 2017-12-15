import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class Stack<Item> implements Iterable<Item> {

	public class Node {
		Item item;
		Node next;
	}
	

	private int count;
	private Node first;
	
	public Stack() { 
		count = 0;
		first = new Node();
	}
	
	public void push(Item item) {
		Node p = new Node();
		p.item = item;
		p.next = first;
		first = p;
		count ++;
	}
	public Item pop() {
		if (isEmpty()) return null;
		Node p = new Node(); 
		p = first;
		first = first.next;
		p.next = null;
		count--;
		return p.item;
	}
	public boolean isEmpty() {  
		return count == 0;
	}
	public int size() {
		return count;
	}

	public Iterator<Item> iterator() {
		return new ListIterator();
	}
	private class ListIterator implements Iterator<Item> {
		private Node current = first;
		public boolean hasNext() {
			return current.next != null;
		}
		public Item next() {
			Item item = current.item;
			current = current.next;
			return item;
		}	
	}
	// 读取一行n个字符串，遇-pop，否则push，最后打印size
	public static void main(String[] args) {
		String s;
		Stack<String> stack = new Stack<String>();
		while (!StdIn.isEmpty()) {
			s = StdIn.readString();
			if (s.equals("-")) stack.pop(); // string.equals(string2);
			else stack.push(s);
		}
		StdOut.println(stack.size());
		for (String k : stack) {
			StdOut.println(k);
		}
	}	
}