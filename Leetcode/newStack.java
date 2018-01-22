public class newStack{
	private Node first;
	private int sum;
	private int N;
	private class Node{
		int point;
		Node next;
	}

	public newStack(){
		first = new Node();
		sum = 0;
		N = 0;
	}
	public int size(){
		return sum;
	}

	public int testsize(){
		return N;
	}
	public void push(int n){
		Node oldfirst = first;
		first = new Node();
		first.point = n;
		first.next = oldfirst;
		sum += n;
		N++;

	}

	public void pop(){
		sum -= first.point;
		first = first.next;	
		N--;
	}

	public int peek_first(){
		if (first != null)
			return first.point;
		else 
			return 0;
	}
	
	public int peek_second(){
		if (first.next != null)
			return first.next.point;
		else
			return 0;
	}

	public String show(){
		String s ="";
		Node p = new Node();
		p = first;
		
		while(p!=null){
			System.out.println(p.point);
			s += p.point + " ";
			p = p.next;
		}
		return s;
	}

}