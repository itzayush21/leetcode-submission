class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        l,r=0,0
        while(r<len(nums)-1):
            f=0
            for i in range(l,r+1):
                f=max(f,i+nums[i])
            l=r+1
            r=f
            res+=1
        return res