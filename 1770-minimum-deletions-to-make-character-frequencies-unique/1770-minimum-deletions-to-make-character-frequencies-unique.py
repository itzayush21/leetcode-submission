class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(s)
        frq=set()
        r=0
        for i,j in count.items():
            while j>0 and j in frq:
                j-=1
                r+=1
            frq.add(j)
        return r
        