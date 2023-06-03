# Solution by Dinar, beats 70%
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = {}
        for i, v in enumerate(manager):
            if v not in G:
                G[v] = [i]
            else:
                G[v].append(i)
        
        def dfs(node, t):
            if node not in G:
                return t
            maxT = 0
            for child in G[node]:
                maxT = max(maxT, dfs(child, maxT))
            return maxT + informTime[node]
        
        return dfs(G[-1][0], 0)