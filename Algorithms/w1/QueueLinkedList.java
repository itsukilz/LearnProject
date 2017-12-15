import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class QueueLinkedList{

	public class Node {
		String item;
		Node next;
	}

	private int count;
	private Node first, last;

	public QueueLinkedList() { 
		count = 0;
		first = new Node();
		last  = new Node();
	}
	public void enqueue(String item) {
		Node p = new Node();
		p.item = item;
		if (count == 0) {
			first = p;
			last = first;
			p.next = null;
		}
		else {
			Node oldlast = last;
			last = p;
			oldlast.next = last;
		}
		count ++;
	}
	public String dequeue() {
		if (isEmpty()) return "";
		Node oldfirst = first;
		first = first.next;
		count--;
		return oldfirst.item;
	}
	public boolean isEmpty() { 
		return count == 0;
	}
	public int size() {
		return count;
	}
	// 读取一行n个字符串，遇- dequeue，否则enqueue，最后打印size
	public static void main(String[] args) {
		String s;
		QueueLinkedList queue = new QueueLinkedList();
		while (!StdIn.isEmpty()) {
			s = StdIn.readString();
			if (s.equals("-")) StdOut.println(queue.dequeue()); 
			else queue.enqueue(s);
		}
		StdOut.println(queue.size());
	}	

}