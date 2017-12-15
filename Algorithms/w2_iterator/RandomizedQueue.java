import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
public class RandomizedQueue<Item> implements Iterable<Item> {
	private Item[] a; 
	private int count;
	public RandomizedQueue() {
		a = (Item[]) new Object[2];
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
		a[count] = item;
		count++;
		if (count >= a.length/2) resize(2*a.length);	
	}

	public Item dequeue() {
		if (count == 0) throw new java.util.NoSuchElementException();
		int randomValue = StdRandom.uniform(count);
		Item item = a[randomValue];
		a[randomValue] = a[count-1];
		a[count-1] = null;
		count--;
		if (count <= a.length/4) resize(a.length/2);
		return item;
	}
	private void resize(int n) {
		Item[] tempa =  (Item[]) new Object[n];
		int k = 0;
		if (n<a.length) k = n;
		else k = a.length;
		
		for (int i =0; i<k; i++) {
			tempa[i] = a[i];
		}
		a = tempa;
	}
	public Item sample() {
		if (count == 0) throw new java.util.NoSuchElementException();
		int randomValue = StdRandom.uniform(count);
		return a[randomValue];
	}

	private class ListIterator implements Iterator<Item> {
		private int[] tempa = StdRandom.permutation(count);
		private int current = 0;
		public boolean hasNext() {
			if (count == 0) return false;
			else return current!= count;
		}

		public Item next() {
			if (current == count) throw new java.util.NoSuchElementException();
			Item item = a[tempa[current]];
			current++;
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
		RandomizedQueue<Integer> rq = new RandomizedQueue<Integer>();
		rq.enqueue(36);
		rq.enqueue(35);
		rq.enqueue(29);    
		rq.dequeue();    
		rq.enqueue(49);
		rq.enqueue(17);
		rq.enqueue(44);		
		// StdOut.println(stack.dequeue());
		// StdOut.println(stack.size());
		// StdOut.println(stack.sample());
		// for (int k : stack) {
		// 	StdOut.println(k);
		// }
		
	}
}