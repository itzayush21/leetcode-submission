class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        map={}
        c=0
        a=[]
        for num in nums:
            if num-k in map:
                if [num,num-k] not in a:
                    c+=1
                    a.append([num,num-k])
            if num in map:
                continue
            map[num]=num
        return c


        