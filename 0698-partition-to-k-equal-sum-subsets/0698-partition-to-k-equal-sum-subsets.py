class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)
        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                # All numbers are placed, check if all buckets are equal to target
                return all(bucket == target for bucket in buckets)
            
            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= nums[index]

                # If bucket is empty, no point in trying other empty buckets
                if buckets[i] == 0:
                    break
            return False
        
        return backtrack(0)