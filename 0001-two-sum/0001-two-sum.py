class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        e={}
        for i,n in enumerate(nums):
            if target-nums[i] in e:
                return(e[target-nums[i]],i)
            e[n]=i
        return