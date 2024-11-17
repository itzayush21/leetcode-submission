class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        sum=0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=matrix[i][j]
                elif matrix[i][j]==1:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                sum+=dp[i][j]
        return sum
        