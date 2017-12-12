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
		p.item = item;
		last.next = p;
		last = p;
		count++;
	}

	public Item dequeue() {
		if (count == 0) throw new java.util.NoSuchElementException();
		int randomValue = StdRandom.uniform(count);

		return out;
	}

	public Item sample() {

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