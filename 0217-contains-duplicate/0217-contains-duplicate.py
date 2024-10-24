class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        return max(count.values())!=1