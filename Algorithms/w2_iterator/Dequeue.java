import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class Dequeue<Item> implements Iterable<Item> {
	private class Node {
		Item item;
		Node next;
		Node before;
	}
	private Node first;
	private Node last;
	private int count;
	public Dequeue() {
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
		first.before = p;
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
		last.next = p;
		p.before = last;
		last = p;
		if (count == 0) first = last;
		count++;
		// StdOut.println(last.item);
	}
	public void removeFirst() {
		if (count == 0) throw new java.util.NoSuchElementException();
		first = first.next;
		count--;
	}
	public void removeLast() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node oldlast = last;
		last = last.before;
		oldlast.next = null;
		count--;
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
		Dequeue<Integer> stack = new Dequeue<Integer>();
		while (!StdIn.isEmpty()) {
			s = StdIn.readInt();
			if (s>5) stack.addFirst(s);
			if (s<5 && s != -1 && s != 0) stack.addLast(s);
			if (s == -1) stack.removeFirst();
			if (s == 0) stack.removeLast();
		}
		for (int k : stack) {
			StdOut.println(k);
		}


	}
		
}