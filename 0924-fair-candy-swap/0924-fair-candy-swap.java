class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        Arrays.sort(aliceSizes);
        Arrays.sort(bobSizes);
        int sum1=0,sum2=0;
        for(int a:aliceSizes)
        {
            sum1+=a;
        }
        for(int b:bobSizes)
        {
            sum2+=b;
        }
        int delta=(sum2-sum1)/2;

        int i=0,j=0;
        while(i<aliceSizes.length && j<bobSizes.length)
        {
            int diff=bobSizes[j]-aliceSizes[i];
            if(diff==delta)
            {
                return new int[]{aliceSizes[i],bobSizes[j]};
            }
            if(diff<delta)
            {
                j++;
            }
            else
            {
                i++;
            }
        }

        return new int[]{-1,-1};
    }
}