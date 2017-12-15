import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.StdOut;

public class PercolationStats {
    private double[] result;
    private double mean, stddev, lo, hi;
    
    private double confidence = 1.96;
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) throw new java.lang.IllegalArgumentException("Illegal n or trials");
        result = new double[trials];
        int x, y;
        Percolation p;
        for (int i = 0; i < trials; i++) {
            p = new Percolation(n);
            
            while (true) {
                int rand = StdRandom.uniform(1, n*n+1);
                if (rand % n == 0) {
                    x = rand / n;
                    y = n;
                }
                else {
                    x = rand / n + 1;
                    y = rand - (x - 1)*n;
                }
    
                p.open(x, y);
                
                if (p.percolates()) {
                    result[i] = (double) p.numberOfOpenSites() / (double) (n*n);
                    break;
                }

            }
            
        }

        mean = StdStats.mean(result);
        stddev = StdStats.stddev(result);
        lo = mean - confidence * stddev / Math.sqrt(trials);
        hi = mean + confidence * stddev / Math.sqrt(trials);
    }

    public double mean() {
        return mean;
    }
    public double stddev() {
        return stddev;
    }
    public double confidenceLo() {
        return lo;
    }
    public double confidenceHi() {
        return hi;
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats p = new PercolationStats(n, trials);
        double mean = p.mean();
        double stddev = p.stddev();
        double lo = p.confidenceLo();
        double hi = p.confidenceHi();
        StdOut.printf("mean\t\t=\t%f\nstddev\t\t=\t%f\n95%% confidence interval\t\t=\t[%f,%f]\n", mean, stddev, lo, hi);
        // StdOut.printf("mean\t\t=\t%f\n",mean);
        // StdOut.printf("stddev\t\t=%f\n",stddev);
        // StdOut.printf("95%% confidence interval\t\t=[%f,%f]\n",lo,hi);
    }
}
