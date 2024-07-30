class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_count=[0]*len(s)
        for i in range(len(s)-2,-1,-1):
            a_count[i]=a_count[i+1]
            a_count[i]+=1 if s[i+1]=="a" else 0
        b_count=0
        res=len(s)
        for i,c in enumerate(s):
            res=min(res,b_count+a_count[i])
            if c == "b":
                b_count+=1
            
        return res