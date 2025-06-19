class Solution {
    public int search(int[] nums, int target) {
        int mid=0;
        for(int i=nums.length-2;i>=0;i--)
        {
            if(nums[i]>nums[i+1])
            {
                mid=i+1;
                break;
            }
        }
        int s=0,e=nums.length-1;
         if (target >= nums[mid] && target <= nums[nums.length - 1]) {
            s = mid;
            e = nums.length - 1;
        } else {
            s = 0;
            e = mid - 1;
        }

        while(s<=e)
        {
            int mid2=s+(e-s)/2;
            if(nums[mid2]==target)
            {
                return mid2;
            }
            else if(nums[mid2]<target)
            {
                s=mid2+1;
            }
            else
            {
                e=mid2-1;
            }
        }
        return -1;
    }
}