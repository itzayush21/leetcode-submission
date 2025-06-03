class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]


        p=list(range(n))
        res=0
        print("p:",p)
        if len(connections)<n-1:
            return -1

        for c in connections:
            a,b=c
            pa, pb = find(a), find(b)
            if pa != pb:
                p[pa] = pb
                res += 1
        print(res)
        return n-1-res
            

        
        