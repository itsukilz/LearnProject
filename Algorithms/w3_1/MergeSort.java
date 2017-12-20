import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;
public class MergeSort {
	private static Comparable[] aux;
	public static void sort(Comparable[] a) {
		aux = new Comparable[a.length];
		sort(a,0,a.length-1);
	}
	private static void sort(Comparable[] a, int lo, int hi) {
		if (hi <= lo) return;
		int mid = (hi-lo)/2 + lo;
		sort(a, lo, mid);
		sort(a, mid+1, hi);
		merge(a, aux, lo, mid, hi); 
	}
	public static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi){
		assert isSorted(a,lo,mid);
		assert isSorted(a,mid+1,hi);
		for (int k=lo; k<=hi; k++) {
			aux[k] = a[k];
		}
		int i = lo; int j = mid+1;
		for (int k=lo; k<=hi; k++) {
			if (i<= mid && j<=hi) {
				if (less(aux[i],aux[j])) {
					
					a[k] = aux[i];
					i++;
				}
				else {

					a[k] = aux[j];
					j++;
				}
			}
			else if (i > mid && j <= hi) {

				a[k] = aux[j];
				j++;
			}
			else if (i <= mid && j > hi) {

				a[k] = aux[i];
				i++;
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
 	public static boolean isSorted(Comparable[] a,int lo, int hi) {
		for (int i=lo+1; i<=hi;i++){
			if (less(a[i],a[i-1])) return false;
		}
		return true;
	}
	public static void main(String[] args) {
		String[] a = In.readStrings();
		sort(a);
		show(a);
	}

}