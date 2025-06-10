class Solution {
    public int maximumWealth(int[][] accounts) {
        int max=Integer.MIN_VALUE;
        
        for(int[] e:accounts)
        {
            int total=0;
            for(int a:e)
            {
                total+=a;
            }
            if(total>max)
            {
                    max=total;
            }
        }
        return max;
    }
}