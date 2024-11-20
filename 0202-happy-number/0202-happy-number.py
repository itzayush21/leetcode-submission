class Solution:
    def isHappy(self, n: int) -> bool:
        res=set()
        if(n==1):
            return True
        while n!=1 and n not in res:
            res.add(n)
            x=[int(i)**2 for i in str(n)]
            n=sum(x)
            if n==1:
                return True
        return False