class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows,cols=len(board),len(board[0])
        path=set()

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or word[i]!=board[r][c]or (r,c) in path:
                return False

            path.add((r,c))

            res=(dfs(r+1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c-1,i+1))

            path.remove((r,c))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False
                
            
        