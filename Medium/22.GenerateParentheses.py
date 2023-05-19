class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [[] for _ in range(n+1)]
        ans[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                for left in ans[i]:
                    for right in ans[k-i-1]:
                        ans[k].append("(" + left + ")" + right)
        
        return ans[-1]
    

class SolutionII:
# @param {integer} n
# @return {string[]}
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")