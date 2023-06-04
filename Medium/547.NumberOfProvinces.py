#Solution by Marlen09
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()  
        def dfs(isConnected, visited, i):
            if i in visited:  
                return 0
            visited.add(i)  
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    dfs(isConnected, visited, j)  
            return 1  
        
        provinces = 0  
        for i in range(len(isConnected)):  
            provinces += dfs(isConnected, visited, i)
        return provinces  
    

# Faster solution by peyman_np, beats 60%
class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans 