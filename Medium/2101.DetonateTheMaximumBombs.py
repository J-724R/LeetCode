# Solution by DBabichev
class Solution:
    def maximumDetonation(self, B: List[List[int]]) -> int:
        n, ans, G = len(B), 0, defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if B[i][2]**2 >= (B[i][0] - B[j][0])**2 + (B[i][1] - B[j][1])**2:
                    G[i] += [j]
        
        
        def dfs(node, visited):
            for child in G[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans
    


# Soltuion by aryan_0077
class Solution:
    def dfs(self, gr, visited, c, i):
        visited[i] = True
        c[0] += 1
        for j in gr[i]:
            if not visited[j]:
                self.dfs(gr, visited, c, j)

    def maximumDetonation(self, bombs):
        n = len(bombs)
        gr = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x, y = bombs[j][0], bombs[j][1]
                    distance_sq = (x - x1) ** 2 + (y - y1) ** 2
                    if distance_sq <= r1 ** 2:
                        gr[i].append(j)

        ans = float('-inf')
        for i in range(n):
            c = [0]
            visited = [False] * n
            self.dfs(gr, visited, c, i)
            ans = max(ans, c[0])

        return ans