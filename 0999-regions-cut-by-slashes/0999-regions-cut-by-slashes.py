class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        row1,col1=len(grid),len(grid[0])
        row2,col2=3*row1,3*col1
        grid2=[[0]*col2 for _ in range(row2)]

        for r in range(row1):
            for c in range(col1):
                r2,c2=3*r,3*c
                if grid[r][c]=="/":
                    grid2[r2][c2+2]=1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2]=1

                if grid[r][c]=="\\":
                    grid2[r2][c2]=1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2+2]=1
                
        def dfs(r,c,visit):
            if (r<0 or c<0 or r==row2 or c==col2 or grid2[r][c]!=0 or (r,c) in visit):
                return
            visit.add((r,c))
            neighbors=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]

            for nr,nc in neighbors:
                dfs(nr,nc,visit)

        
        visit=set()
        res=0
        for r in range(row2):
            for c in range(col2):
                if grid2[r][c]==0 and (r,c) not in visit:
                    dfs(r,c,visit)
                    res+=1
        return res

        