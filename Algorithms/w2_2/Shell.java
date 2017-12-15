import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;
public class Shell {
	public static void sort(Comparable[] a){
		int n = a.length;
		for (int h = ((n / 3) -1 )* 3 + 1; h > 0; h = h-3) {
			for (int i = 0; i<a.length; i++) {
				for (int j=i; j-h>=0; j=j-h) {
					if (less(a[j],a[j-h]))
						exch(a,j,j-h);
					else break;
				}
			}
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
		sort(a);
		assert isSorted(a);
		show(a);
	}

}