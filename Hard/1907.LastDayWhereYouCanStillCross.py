# Solution by DBabichev
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def latestDayToCross(self, n, m, C):
        row, col = len(C), len(C[0])
        dsu = DSU(m*n + 2)
        grid = [[1] * m for _ in range(n)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]
        C = [(x-1, y-1) for x, y in C]

        def index(x, y):
            return x * m + y + 1

        for i in range(len(C) - 1, -1, -1):
            x, y = C[i][0], C[i][1]

            grid[x][y] = 0
            for dx, dy in neibs:
                ind = index(x+dx, y+dy)
                if x+dx>=0 and x+dx<n and y + dy >= 0 and y + dy < m and grid[x+dx][y+dy] == 0:
                    dsu.union(ind, index(x, y))
            if x == 0:
                dsu.union(0, index(x, y))
            if x == n - 1:
                dsu.union(m*n + 1, index(x, y))

            if dsu.find(0) == dsu.find(m*n + 1):
                return i
            
# Faster solution by ye15, beats 83.70%
class UnionFind: 
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p]) # find w/ path compression 
        return self.parent[p]
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False # already connected 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # union by rank 
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 
    

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0]*col for _ in range(row)]
        
        n = row * col
        uf = UnionFind(n)
        span = [[n, 0] for _ in range(n)]
        
        for step, (i, j) in enumerate(cells): 
            i, j = i-1, j-1
            grid[i][j] = 1
            x = i*col + j
            for ii, jj in (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1): 
                if 0 <= ii < row and 0 <= jj < col and grid[ii][jj]: 
                    xx = ii*col + jj 
                    r, rr = uf.find(x), uf.find(xx)
                    span[r][0] = span[rr][0] = min(span[r][0], span[rr][0], j, jj)
                    span[r][1] = span[rr][1] = max(span[r][1], span[rr][1], j, jj)
                    if span[r] == [0, col-1]: return step 
                    uf.union(x, xx)