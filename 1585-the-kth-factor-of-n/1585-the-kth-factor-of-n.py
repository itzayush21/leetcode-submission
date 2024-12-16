class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(1,n+2):
            if k==0:
                print(1)
                return c
            if n%i==0:
                c=i
                k-=1
        return -1
        