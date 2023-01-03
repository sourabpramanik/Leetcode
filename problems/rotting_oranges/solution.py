class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=collections.deque()
        drow=[-1, 0, 1, 0]
        dcol=[0, 1, 0, -1]
        days=0
        cnt=0
        tot=0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j]==2:
                    queue.append((i, j))
                if grid[i][j]!=0:
                    tot+=1
        
        while queue:
            size=len(queue)
            cnt+=size
            while size:
                tup=queue.popleft()
                for i in range(0, 4):
                    nrow=drow[i]+tup[0]
                    ncol=dcol[i]+tup[1]
                    if self.valid(nrow, ncol, grid, m, n):
                        grid[nrow][ncol]=2
                        queue.append((nrow, ncol))
                size-=1

            if len(queue)!=0:
                days+=1
        if tot==cnt:
            return days
        return -1

    def valid(self, row, col, grid, m, n):
        if row<0 or col<0 or row>=m or col>=n or grid[row][col]!=1:
            return False
        return True