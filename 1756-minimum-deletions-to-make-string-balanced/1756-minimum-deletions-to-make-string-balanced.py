class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_count=0
        for i in range(len(s)):
            a_count+=1 if s[i]=="a" else 0
        b_count=0
        res=len(s)
        for i,c in enumerate(s):
            if c=="a":
                a_count-=1
            res=min(res,b_count+a_count)
            if c == "b":
                b_count+=1
            
        return res