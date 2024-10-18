class Solution:
    def divisorGame(self, n: int) -> bool:
        if n<=1:
            return False
        for i in range(1,n):
            if n%i==0:
                return not Solution.divisorGame(self,n-i)
        return False
        