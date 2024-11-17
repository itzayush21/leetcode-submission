class Solution:
    def reverse(self, x: int) -> int:
        res=0
        n=x<0
        x=abs(x)
        while(x!=0):
            rem=x%10
            res=(res*10)+rem
            x=x//10
        if n==True:
            res=-res
        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res