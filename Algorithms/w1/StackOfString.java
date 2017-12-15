import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
public class StackOfString {

    public class Node {
            String item;
            Node next;
        }

    private int count;
    private Node first;

    public StackOfString() {
            count = 0;
            first = new Node();
        }
    public void push(String item) {
            Node p = new Node();
            p.item = item;
            p.next = first;
            first = p;
            count ++;
        }
    public String pop() {
            if (isEmpty()) return "";
            Node p = new Node();
            p = first;
            first.next = p.next;
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
// 读取一行n个字符串，遇-pop，否则push，最后打印size
    public static void main(String[] args) {
            String s;
            StackOfString stack = new StackOfString();
            while (!StdIn.isEmpty()) {
                        s = StdIn.readString();
                        if (s.equals("-")) stack.pop(); // string.equals(string2);
                        else stack.push(s);
                    }
            StdOut.println(stack.size());
        }
}
