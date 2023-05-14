class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                result += 1
            elif result:
                return result

        return result

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      return 0 if len(s.split())==0 else len(s.split()[-1])