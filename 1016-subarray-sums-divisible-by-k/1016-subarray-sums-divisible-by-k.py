class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre,res=0,0
        d={}
        d[0]=1
        for n in nums:
            pre+=n
            remain=pre%k

            if remain in d:
                res+=d[remain]
                d[remain]+=1
            else:
                d[remain]=1
            
        return res

        