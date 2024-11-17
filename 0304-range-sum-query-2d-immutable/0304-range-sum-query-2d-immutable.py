class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n=len(matrix),len(matrix[0])
        self.dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            prefix=0
            for j in range(n):
                prefix+=matrix[i][j]
                above=self.dp[i][j+1]
                self.dp[i+1][j+1]=prefix+above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        res=self.dp[row2][col2]
        above=self.dp[row1-1][col2]
        left=self.dp[row2][col1-1]
        topleft=self.dp[row1-1][col1-1]
        return res-above-left+topleft
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)