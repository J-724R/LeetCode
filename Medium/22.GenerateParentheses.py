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