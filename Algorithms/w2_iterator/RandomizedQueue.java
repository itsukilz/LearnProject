import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
public class RandomizedQueue<Item> implements Iterable<Item> {
	private class Node {
		Item item;
		Node next;
	}
	private Node first;
	private Node last;
	private int count;
	public RandomizedQueue() {
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

	public void enqueue(Item item) {
		if (item == null) throw new java.lang.IllegalArgumentException();
		Node p = new Node();
		Node empty = new Node();
		p.item = item;
		p.next = empty;
		last.next = p;
		last = p;
		if (count == 0) first = last;
		count++;
	}

	public Item dequeue() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node before = randomNode();
		
		Item item = before.next.item;
		before.next = before.next.next;
		return item;


	}
	private Node randomNode() {
		if (count == 1) return first;
		else {
			int randomValue = StdRandom.uniform(count-1);
			int stopCount = 1;
			Node start = first;
			Node temp;
			while (stopCount < randomValue-1) {
				temp = start.next;
				start = temp;
				stopCount++;
			}
			return start;
		}
	}
	public Item sample() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node before = randomNode();
		return before.next.item;		

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
		RandomizedQueue<Integer> stack = new RandomizedQueue<Integer>();
		while (!StdIn.isEmpty()) {
			s= StdIn.readInt();
			if (s != -1 && s != 0) stack.enqueue(s);
		}
		for (int k : stack) {
			StdOut.println(k);
		}
		// StdOut.println(stack.dequeue());
		StdOut.println(stack.sample());
		for (int k : stack) {
			StdOut.println(k);
		}
		
	}
}