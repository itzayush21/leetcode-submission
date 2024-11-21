class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0 or n<0:
            return False
        return ceil(math.log2(n))==floor(math.log2(n))