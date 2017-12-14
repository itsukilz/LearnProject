import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
public class RandomizedQueue<Item> implements Iterable<Item> {
	private class Node {
		Item item;
		Node next;
		Node before;

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
		if (count == 0) {
			last = p;
			first = last;
		}
		else {
			last.next = p;
			p.before = last;
			last = p;
		}
		count++;
	}

	public Item dequeue() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node deleteNode = randomNode();
		if (deleteNode == first) {
			Node oldfirst = first;
			first = first.next;
			count--;
			return oldfirst.item;
		}
		else if (deleteNode == last) {
			Node oldlast = last;
			last = last.before;
			count--;
			return oldlast.item;			
		}
		else {
			Node oldNode = deleteNode;
			deleteNode.before.next = deleteNode.next;
			deleteNode = null;
			count--;
			return oldNode.item;
		}
	}
	private Node randomNode() {
		int randomValue = StdRandom.uniform(count)+1;
		int stopCount = 1;
		Node start = first;
		Node temp;
		while (stopCount < randomValue) {
			temp = start.next;
			start = temp;
			stopCount++;
		}
		return start;
	}
	public Item sample() {
		if (count == 0) throw new java.util.NoSuchElementException();
		Node chosenNode = randomNode();
		return chosenNode.item;

	}

	private class ListIterator implements Iterator<Item> {
		private Node current = first;
		public boolean hasNext() {
			return current!= null;
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
			stack.enqueue(s);
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