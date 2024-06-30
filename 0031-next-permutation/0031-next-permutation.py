class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                ind=i
                break
        if ind==-1:
            nums.reverse()
            return nums
        for j in range(len(nums)-1,ind,-1):
            if(nums[j]>nums[i]):
                nums[i],nums[j]=nums[j],nums[i]
                break
        nums[i+1:len(nums)]=nums[i+1:len(nums)][::-1]
        return nums
            