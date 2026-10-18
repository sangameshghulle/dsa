class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        
        def bfs(grid,start):
            r,c=start[0],start[1]
            q=deque([start])
            grid[r][c]='0'
            dir=[(0,1),(0,-1),(1,0),(-1,0)]

            while q:
                sr,sc=q.popleft()
                
                for nr,nc in dir:
                    dr,dc=sr+nr,sc+nc
                    if (0<=dr<rows and 0<=dc<cols and grid[dr][dc]=='1'):
                        grid[dr][dc]='0'
                        q.append((dr,dc))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    islands+=1
                    bfs(grid,(i,j))
        
        return islands