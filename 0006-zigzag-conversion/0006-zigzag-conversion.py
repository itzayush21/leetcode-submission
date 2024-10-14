class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n=len(s)
        res=""
        if numRows==1:
            return s
        incre=2*(numRows-1)
        for i in range(numRows):
            for r in range(i,n,incre):
                res+=s[r]
                if i>0 and i<numRows-1 and r+incre-2*i<n:
                    res+=s[r+incre-2*i]
        return res


        