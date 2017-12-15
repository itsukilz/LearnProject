import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdRandom;
public class Shuffle {
	public static void KnuthShuffle(Comparable[] a){
		for(int i = 0; i < a.length; i++) {
			int r = StdRandom.uniform(0,i+1);
			exch(a,i,r);
		}
	}
	private static boolean less(Comparable v, Comparable w) {
		return v.compareTo(w) < 0;	
	}
	private static void exch(Comparable[] a, int i, int j){
		Comparable t = a[i];
		a[i] = a[j];
		a[j] = t;
	}
	private static void show(Comparable[] a) {
		for (int i=0; i<a.length; i++){
			StdOut.print(a[i]+" ");
		}
		StdOut.println();
 	}
 	public static boolean isSorted(Comparable[] a) {
		for (int i=0; i<a.length;i++){
			if (less(a[i],a[i-1])) return false;
		}
		return true;
	}
	public static void main(String[] args) {
		String[] a = In.readStrings();
		KnuthShuffle(a);
		show(a);
	}

}