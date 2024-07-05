class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        top=0
        l=0
        r=len(matrix[0])-1
        b=len(matrix)-1
        while top<=b and l<=r:
            for i in range(l,r+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,b+1):
                res.append(matrix[i][r])
            r-=1
            if top<=b:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in range(b,top-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res