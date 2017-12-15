import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class Bag<Item> implements Iterable<Item> {
	private Node first;
	private int count;
	
	public class Node {
		Item item;
		Node next;
	}
	public Bag() {
		first = new Node();
		count = 0;
	}
	public void add(Item item) {
		Node p = new Node();
		p.item = item;
		p.next = first;
		first = p;
		count++;
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
	public static void main(String[] args) {
		String s;
		Bag<String> bag = new Bag<String>();
		while (!StdIn.isEmpty()) {
			s = StdIn.readString();
			if (!s.equals("-")) bag.add(s); // string.equals(string2);
		}
		StdOut.println(bag.size());
		for (String k : bag) {
			StdOut.println(k);
		}
	}	
}