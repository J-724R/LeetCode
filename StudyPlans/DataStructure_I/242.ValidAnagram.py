from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      st1, st2 = Counter(s), Counter(t)
      if st2 == st1:
          return True
      return False