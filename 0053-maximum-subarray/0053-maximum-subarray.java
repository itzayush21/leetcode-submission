class Solution {
    public int maxSubArray(int[] nums) {
        int max=Integer.MIN_VALUE;
        int sum=0;
        if(nums.length == 1){
            return nums[0];
        }
        for(int e:nums)
        {
            sum+=e;
            max=Math.max(max,sum);
            if(sum<0)
            {
                sum=0;
            }
        }
        return max;
    }
}