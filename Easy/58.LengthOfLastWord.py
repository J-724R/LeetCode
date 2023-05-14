class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                result += 1
            elif result:
                return result

        return result

class SolutionII:
    def lengthOfLastWord(self, s: str) -> int:
      return 0 if len(s.split())==0 else len(s.split()[-1])
    
# Without built in methods
class SolutionIII:
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end > 0 and s[end] == " ": end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ": beg -= 1
        return end - beg