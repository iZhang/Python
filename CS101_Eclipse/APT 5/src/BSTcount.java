public class BSTcount {
    long[] storedInfo;

    public long howMany(int[] values) {     
        int n = values.length;
        storedInfo = new long[n];       
        return calculate(n);
    }

    private long calculate(int n) {
        if (n == 0)
            return 1;
        
        if (storedInfo[n-1]!=0){
            return storedInfo[n-1];
        }

        long total = 0;
        int left = 0;
        int right = 0;
        for (int k = 0; k < n; k++) {
            left = k;
            right = n - k - 1; // -1 is for the root
            total += calculate(left) * calculate(right);
        }
        storedInfo[n-1] = total;
        return total;
    }
}