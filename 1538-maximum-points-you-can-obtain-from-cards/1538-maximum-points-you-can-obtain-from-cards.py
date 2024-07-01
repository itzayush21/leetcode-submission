class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        ts,rs,ls=0,0,0
        if k==len(cardPoints):
            return sum(cardPoints)
        l,r=0,len(cardPoints)
        ls=sum(cardPoints[:k])
        ts=ls
        for i in range(k-1,-1,-1):
            ls-=cardPoints[i]
            r-=1
            rs+=cardPoints[r]
            ts=max(ts,ls+rs)
        
        return (ts)

                
        
                


            


