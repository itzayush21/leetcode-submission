class Solution {
    public int numIdenticalPairs(int[] nums) {
        int freqs []= new int[101];
        int max = -1;int min = Integer.MAX_VALUE;
        Arrays.fill(freqs,-1);
        for(int i:nums) 
        {   if(freqs[i]==-1) freqs[i]=0;
            freqs[i]++;
            
            max = Math.max(max,i);
            min = Math.min(min,i);
        }
        int res=0;
        for(int i=min;i<=max;i++){
            if(freqs[i]>0) res+= (freqs[i]*(freqs[i]-1))/2;//n*(n-1)/2
        }
        return res;
    }
}