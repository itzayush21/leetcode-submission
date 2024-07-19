class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        com=[]
        def track(o,c,path):
            if o > n or c > n or o < c:
                return 
            if o == n and c==n:
                com.append(path)
                return
            track(o+1,c,path+"(")
            track(o,c+1,path+")")
        track(0,0,"")
        return com