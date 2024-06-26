class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r,c=len(board),len(board[0])
        def count(x, y):
            nei=0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if((i==x and j==y) or i<0 or j<0 or
                        i==r or j==c):
                        continue
                    if board[i][j] in [1,3]:
                        nei+=1
            return nei


        for i in range(r):
            for j in range(c):
                nei=count(i,j)
                if board[i][j]:
                    if nei in [2,3]:
                        board[i][j]=3
                elif nei==3:
                    board[i][j]=2
        for i in range(r):
            for j in range(c):
                if board[i][j]==1:
                    board[i][j]=0
                elif board[i][j] in [2,3]:
                    board[i][j]=1
