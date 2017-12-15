import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Percolation {
	private boolean[][] grid;
	private int size;
	private WeightedQuickUnionUF uf;
	private WeightedQuickUnionUF uf2;
	private int opencount;

	public Percolation(int n) {

		if (n <= 0) throw new java.lang.IllegalArgumentException("n <= 0");

		grid = new boolean[n+1][n+1];
		size = n;
		uf = new WeightedQuickUnionUF(n*n+2);
		uf2 = new WeightedQuickUnionUF(n*n+2);
		opencount = 0;

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				grid[i][j] = false;
			}
		}
	}


	private void checkIllegal(int row, int col) {
		if (!(row <= size && row >= 1 && col <= size && col >= 1)) throw new java.lang.IllegalArgumentException("number is illegal.");
	}

	private int map(int row, int col) {

		return size * (row - 1) + col;
	}

	public boolean isOpen(int row, int col) {
		checkIllegal(row, col);
		return grid[row][col];
	}

	public void open(int row, int col) {
		checkIllegal(row, col);
		if (isOpen(row, col)) return;
		
		else {
			grid[row][col] = true;
			opencount++;

			int x = map(row, col);

			// first line and last line
			if (row == 1) {
				uf.union(0, x);
				uf2.union(0, x);
			} 
			if (row == size) uf.union(size*size+1, x);
			//  four directions
			if (row > 1 && isOpen(row-1, col)) {
				uf.union(x, x-size);
				uf2.union(x, x-size);
			}
			if (row < size && isOpen(row+1, col)) {
				uf.union(x, x+size);
				uf2.union(x, x+size);
			}
			if (col > 1 && isOpen(row, col-1)) {
				uf.union(x, x-1);
				uf2.union(x, x-1);
			}
			if (col < size && isOpen(row, col+1)) {
				uf.union(x, x+1);
				uf2.union(x, x+1);
			}
		}
	}

	public boolean isFull(int row, int col) {
		checkIllegal(row, col);
		if (!isOpen(row, col)) return false;
		int x = map(row, col);
		return uf2.connected(0, x);

	}

	public boolean percolates() {
		return uf.connected(0, size*size+1);
	}

	public int numberOfOpenSites() {
		return opencount;
	}

	public static void main(String[] args) {
		int a, b, n, flag;
		n = StdIn.readInt();
		Percolation p = new Percolation(n);
		flag = 0;

		while (!StdIn.isEmpty()) {
			a = StdIn.readInt();
			b = StdIn.readInt();
			p.open(a, b);
			
			// StdOut.println(p.isFull(a, b));
			if (p.percolates()) {
				flag = 1;
				break;
			}
			
		}

		if (flag == 1) StdOut.println("yes");
		else StdOut.println("no");
	}
}