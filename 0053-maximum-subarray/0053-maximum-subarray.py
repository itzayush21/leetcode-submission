class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        m=-10000
        for i in nums:
            sum+=i
            m=max(m,sum)
            if sum<0:
                sum=0
        return m