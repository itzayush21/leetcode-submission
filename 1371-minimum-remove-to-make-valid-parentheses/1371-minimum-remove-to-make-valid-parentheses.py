class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        open_b,l=0,[]
        for i in s:
            if i=='(':
                l.append(i)
                open_b +=1
            elif i==')' and open_b>0:
                l.append(i)
                open_b -=1
            elif i!=')':
                l.append(i)                
        res=[]
        for j in l[::-1]:
            if j=='(' and open_b>0:
                open_b-=1
            else:
                res.append(j)

        return "".join(res[::-1])