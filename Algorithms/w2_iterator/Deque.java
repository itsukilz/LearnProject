import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class Deque<Item> implements Iterable<Item> {
	private class Node {
		Item item;
		Node next;
		Node before;
	}
	private Node first;
	private Node last;
	private int count;
	public Deque() {
		first = new Node();
		last = new Node();
		count = 0;
	}
	public boolean isEmpty() {
		return count == 0;
	}
	public int size() {
		return count;
	}
	public void addFirst(Item item) {
		if (item == null) throw new java.lang.IllegalArgumentException();
		Node p = new Node();
		p.item = item;
		p.next = first;
		if (first != null)first.before = p;
		first = p;
		if (count == 0) last = first;
		count++;
		// StdOut.println(first.item);
	}
	public void addLast(Item item) {
		if (item == null) throw new java.lang.IllegalArgumentException();
		Node p = new Node();
		p.item = item;
		p.next = null;
		if (last != null) last.next = p;
		p.before = last;
		last = p;
		if (count == 0) first = last;
		count++;
		// StdOut.println(last.item);
	}
	public Item removeFirst() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node oldfirst = first;
		first = first.next;
		count--;
		return oldfirst.item;
	}
	public Item removeLast() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node oldlast = last;
		last = last.before;
		oldlast.next = null;
		count--;
		return oldlast.item;
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
		public void remove() {
			throw new java.lang.UnsupportedOperationException();
		}
	}
	public Iterator<Item> iterator() {
		return new ListIterator();
	}
	public static void main(String[] args) {
		int s;
		Deque<Integer> stack = new Deque<Integer>();
		StdOut.println(stack.isEmpty());
		stack.addFirst(8);
		StdOut.println(stack.size());

	}
		
}